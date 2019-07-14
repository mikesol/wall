# Validation

Wall's killer feature is validation of input.  For safe code, meaning code that exists only within the walls of Wall, validation is done at compile time. For unsafe code, meaning code that does some form of IO, the same validators that you use for your safe code can easily be used for your unsafe code.  Validators can even correct bad input or create monads with error messages that can flow through a program until termination.

Best of all, validators are plain old Wall objects.  If you've followed this documentation interactively, you've used several already.

If we revisit our original example of `def`:

```
w> foo = def _? int? fed @ { a0 %%k a1 %k } (> a1 5).? 0 a0
w> foo {} 6
{}
w> foo {} 5
{}
```

We see two validators: `_?` and `int?`. `_?` is an object that has every `thing` as a key and `true` for every value. `int?` also has every `thing` as a key, but only `true` values for things that are in the set `int`.  All validators must have every `thing` as a key pointing to a `bool` value.

```
w> int? 5
true
w> _? 'foo
true
w> int? 'foo
false
```

The predefined function `:` will force a compilation error if a value does not pass the validator. This can be a useful form of documentation when working in teams or if you, like most people, are forgetful.

```
w> foo = : int? 5
w> foo
5
w> <5? = def! 'a0 _? fed < a0 5
w> bar = : <5? 5
Error. The key 5 does not exist on the object `:` <5?.
```
 
## Wall ♥️ validators

The Wall compiler is so crazy about validators that, when they are present, it does all sorts of cool things to show its love.  It even automatically inserts them when they are *not* present.

For starters, named `thing`-s retain the strongest possible validation in a compilation chain.  That means that, if something is validated to be equal to `5`, then an `int`, then a `thing`, it will retain the validation of being equal to `5`.

```
w> is5? = omap! thing { k false } .& { 5 true }
w> id5 = def! 'i is5? fed i
w> idint = def! 'i int? fed i
w> idthing = def! 'i int? fed i
w> 5back = 5.idint.idthing.id5
w> 5back 5
5
w> 6back = 6.idint.idthing.id5
Error. The object `id5` does not contain the key `6`.
```

Next up, if a `thing` is part of a structure that will ultimately resolve to a boolean and it lacks the appropriate validators, they will be added automatically with `&`-s. As a result, the following two statements are equivalent:

```
w> d? = def! 'a _? fed (== (- a 5) 3)
w> e? = def! 'a _? fed (& (int? a) (== (- a 5) 3))
w> d? 'foo
false
w> d? 10
false
w> d? 8
true
w> d? == (?ify [8])
true
```

## Rolling your own validators

We can write our own validators:

```
w> <5? = def! 'a0 _? fed (& (int? a0) (< a0 5))
w> <5? 4
true
w> <5? 5
false
w> 5?
```

We could have written our validator like this as well.

```
w> <5? = & (map! thing { k false }) (map! int { k (< k 5) })
```

The pattern in this example is common in Wall. Take a union of two `object`-s, where:

- one `object` that maps every `thing` to `false`.
- one `object` that maps every `int` to `true` if the `int` is less than `5`, otherwise `false`.

This pattern can also be accomplished using the `?ify` object, which creates a validator from a set that should validate positively.

```
w> <5? = ?ify int.$map! (? (< k 5) k $)
```

Now, let's rewrite `foo$` from above using a custom validator:

```
w> <5? = def! 'a0 _? fed (& (int? a0) (< a0 5))
w> foo$ = def! 'a0 _? 'a1 <5? fed (? (> a1 5) 0 a0)
w> foo$ 'hello -1
'hello
w> foo$ {} 1
0
w> foo$ {} 10
Error. The key 10 does not exist on the object `foo$` {}. 
```

## Strategies for making validators

There are two common strategies to make a validator:

- Create a `set` of elements that are valid (ie a `set` called `foo`), and call `?ify foo`. This creates an object that maps all `thing`-s to `false *except* the things in the `set`.
- Define a function that yields an object mapping all elements to either `true` or `false`.
 
### `?fy` strategy

```
w> a0? = ?ify [{ 'a 0 }]
w> a0? { 'a 0 }
true
w> a0? 0
false
w> n_n+1? = ?ify (val (def! 'n int? fed { 'n n 'n+1 (+ n 1) }))
w> n_n+1? { 'n 0 'n+1 1 }
true
w> n_n+1? { 'n 0 'n+1 2 }
false
w> n_n+1? 0
false
```
 
### `def!` strategy

```
w> a0? = def! 'a _? { a (a == { a' 0 }) }
w> a0? { 'a 0 }
true
w> a0? 0
false
w> n_n+1? = def! 'a _? { a (== (a 'n+1) (+ 1 (a 'n))) }
w> n_n+1? { 'n 0 'n+1 1 }
true
w> n_n+1? { 'n 0 'n+1 2 }
false
w> n_n+1? 0
false
```

### Validating recursive `object`-s

You may remember that a the constructor of a linked list can be defined like so.

```
w> ; = 
w> z = omap! thing @ { c $%% ; } { k (z .& { ; { a c } } ) } .& { ; {} }
```

This is one of many ways to define a link list's constructor, and intuitively, we may want to ask "is an object a linked list according to this definition"?

One way to do this is to use `?ify` on the values of the aggregator keys `;` that exist on the recursive `object`-s that comprise `z`.  Another way to do this is to create a validator describing the list's properties.  the results will be the same.

```
w> ll1 = @{ p %! }
  (omap! thing { k (%k ;)
    .$& @ { b %% } (red!! (b .~ ;).val aa .& (p kk) []) }) z
w> ll1? = ?ify ll1
w> ll1? { 1 { 2 { 3 {} } } }
true
w> ll2 = def 'a thing? fed (== a {}) .| (& (a.len.== 1) (ll2 a.choose))
w> ll2? = ?ify ll2
w> ll2? { 1 { 2 { 3 {} } } }
w> == ll1? ll2?
true
```

The object assigned to `ll1?` is so useful that there is a prepackaged object called `rag` that does exactly this.  `rag` is short for "reverse aggregator".  It reinforces a common pattern in Wall: define a recursive `object` constructor with a symbol that acts as an aggregator, and then use `all` to define the set of objects that the aggregator can hold.