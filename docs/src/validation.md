# Validation

Wall's killer feature is validation of input.  For safe code, meaning code that exists only within the walls of Wall, validation is done during compile time. For unsafe code, meaning code that does some form of IO, the same validators that you use for your safe code can easily be used for your unsafe code.  Validators can even correct bad input or create monads with error messages that can flow through a program until termination.

Best of all, validators are plain old Wall objects.  If you've followed this documentation interactively, you've used several already.

If we revisit our original example of `def`:

```
w> foo$ = def! 'a0 _? 'a1 int? fed (? (> a1 5) 0 a0)
w> foo$ {} 6
{}
w> foo$ {} 5
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

For starters, if a validator evaluates as `true` anywere in the heirarchy of an `object`'s structure, the lower `object`-s will assume that the validated object is in the `set` described by that validator. Alternatively, if the validator validates as `false`, then the lower `object`-s will assume that the validated `object` is in the complement of the `set` described by that validator. This is guaranteed by Wall's static typing system.

```
w> a = 5
w> b = 'foo
w> c = (? (((map! thing { k false }) & { 5 true }) a) a b)
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

The last bit brings up an important aspect of Wall that is commonly referred to as **duck-typing**.  That is, if it quacks like a duck and walks like a duck, it's a duck.  In the example above, both `d?` and `?ify [8]` create the same object.  However, because we can never *see* the object because of its infinite size, we can only describe it.  Thus, if it has all of the keys and values of `(map! thing { a false }) & { 8 true }`, then it *is* that.

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
w> <5? = & (map! { a false } thing) (map! { a (< a 5) } int)
```

The pattern in this example is common in Wall. Take a union of two `object`-s, where:

- one `object` that maps every `thing` to `false`.
- one `object` that maps every `int` to `true` if the `int` is less than `5`, otherwise `false`.

This pattern can also be accomplished using the `?ify` object, which creates a validator from a set that should validate positively.

```
w> <5? = ?ify (map! int (? (< k 5) k $)) 
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