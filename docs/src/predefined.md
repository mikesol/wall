 
# Predefined things

Some `thing`-s in Wall are predefined. That is, they are defined by the Wall maintainers for you.  They are predefined for several reasons:

- they would be really difficult or bothersome to define; and/or
- the maintainers have an opinionated veiw about how they should be defined.

For example, think about the following object:

```
w> < = { 0 { 1 true } 1 { 2 true 0 false } }
w> < 0 1
true
w> < 1 0
false
w> 1 .< 2
true
```

This object works very much like the relation `<`, or less-than. `0` is less than `1`, `1` is not less than `0`, etc. However, this object would become difficult to manually define for every imaginable integer.  Indeed, it would be impossible. That's why Wall has predefined `object`-s and, more generally, predefined `thing`-s.
 
## `float`

Wall comes with a few predefined `float`-s that are sometimes useful.

```
w> rand
0.055325461
w> now
1562524244.200712
```

Because Wall evaluates lazily, these `float`-s will evaluate only when they need to. To force evaluation, you can use the `bang` hint.

```
w> ! rand
0.055325461
w> ! now
1562524244.200712
```
 
## `object`

Wall has lots of predefined `object`-s.  In this section, we'll cover several of the most popular predefined objects.  A full reference of predefined objects can be found [here](/reference). In the [Examples](/examples) section, we will create our own versions of some predefined objects.

### `key` and `val`

The `set` of an `object`-s keys is represented by the `key` `object`. The `set` of an `object`-s values is represented with the `val` `object`.

```
w> key { 1 2 3 4 }
[1 2]
w> { 1 2 3 4 }.val
[3 4]
```

### `choose`

Choose is an object that associates a `set` or an `object` with a random element from that `set` or a random key from that `object`.

```
w> choose [1 2 3]
1
w> choose [1 2 3]
2
w> choose [1 2 3]
1
w> choose { 1 2 3 4 5 6 }
5
w> choose { 1 2 3 4 5 6 }
3
w> choose { 1 2 3 4 5 6 }
3
```

Importantly, `choose []` is `$` and `choose {}` is `$`.

```
w> choose []
$
w> choose {}
$
w> choose [$]
$
w> choose { $ 1 }
$
w> choose { 1 $ }
$
```
 
### `suc`

`suc` is an `object` representing the successor function. Its keys are all members of `int` and `float`.

```
w> suc 1
2
w> suc -999.999
w> -998.999
```

### `pre`

`pre` is an `object` representing the predecessor function. Its keys are all members of `int` and `float`.

```
w> pre 1
0
w> pre -999.999
w> -1000.999
```

### `d-1`, `d-2` and `d-n`

Arbitrary delayed application of `object` keys can be created with the family of `d-` `object`-s.

```
w> a = d-1 [0 'foo].& key
w> a { 3 4 }
[0 'foo 3]
w> b = d-2 [0].+ map
w> b [5 6] 2.*
[0 10 12]
w> c = d-2 7.* +
w> c 3 2
42
```

Here, we are saying "take the last key, apply `-n` keys to it, and then use it as a key in the preceding key.

### `not`, `&`, `|`, `x|`, `xn|`, `if` and `iff`

The operators `not`, `&`, `|`, `x|`, `xn|`, `if` and `iff` all work on `bool`, and some of them pull triple duty for `bool`, `set` and `object`.

```
w> & true false
false
w> [0].& [1]
[0 1]
w> x| false false
true
```

The `object` union operator also has a recursive variant that merges objects and sets with similar keys when possible instead of replacing the content.

```
w> &! { 0 { 1 2 'foo ['bar] }} { 0 { 3 4 'foo ['baz] }}
{0 { 1 2 3 4 'foo ['bar 'baz] }}
```

### `==` and `/=`

Wall defines equality as "being the same or containing the same things."

```
w> == 1 1
true
w> == 1 (+ 0 1)
true
w> [1 2 3].== [1 2 (+ 1 2)]
true
w> == [1 2 3] [3 2 1 $]
true
w> { 0 { 0 1 } } .== { 0 { 0 1 } }
true
w> == (d-2 not >=) <
true
w> == (d-2 not >) <
false
```

### `def`

`def` is a predefined object that, intuitively, describes something that resembles a function in other languages. As a convention, all function names should end with `$`.

```
w> foo$ = def _? int? fed @ { a0 %%k a1 %k } (> a1 5).? 0 a0
w> foo$ {} 6
{}
w> foo$ {} 5
{}
```

In other languages, we would say something like:

> `foo$` is a function that takes two arguments, where the first can be anything and the second must be an integer. It returns `0` if the second argument is greater than `5`, else it returns the first argument.

In Wall, we'd say:

> `foo$` is a nested object. `k` can be anything. `v.k` must be an integer. And `v.v` is `0` or `k` depending if `v.k` is greater than `5`.

Sometimes, it is useful to work with named arguments.  There is a version of `def` called `def!` that does that too by applying `@` internally.

```
w> foo$ = def! 'a0 _? 'a1 int? fed (? (> a1 5) 0 a0)
w> foo$ {} 6
{}
w> foo$ {} 5
{}
```
 
### `rev+` and `rev-`

`rev+` takes a three-level deep object and reverses application of two keys.

```
w> { 'a { 'b 0 } }.rev+ 'b 'a
0
w> < 5 4
false
w> rev+ < 5 4
true 
```

`rev-` reverses the previous key with the incoming key of a binary function.

```
w> < 5 4
false
w> rev- (< 5) 4
true
```
 
### `red`

Sometimes, you want to reduce the key/value pairs in an `object` or `set`, like summing them up. That's done with `red`.  It takes either a `set` or `object as its first key, an accumulator `object` as its second key, and an initial value for an accumulator as its third key.

```
w> red [1 2 3] + 0
6
w> red [{'a 1} {'b 2} {'c 3}] & {}
{'a 1 'b 2 'c 3}
```

Sometimes, we want to pass an ad-hoc object to `red`:

```
w> red { 0 1 2 3 4 5 } def 'a object? 'k int 'v int fed & a { k (? k .== 4 v .* 10 $) }
{ 4 50 }
```

In this case, the syntax `red!` saves us some space - it automatically injects three values into the context.

- `a`: the accumulator
- `k`: the key
- `v`: the value

```
w> red! { 0 1 2 3 4 5 } & a { k (? k .== 4 v .* 10 $) }
```

### `map`

`map` is used to apply each element of a `set` or each key-value pair of an `object` to an `object.

```
w> map [8 3 2] 3.>
[false false true]
```

`map` also has a `!` equivalent, `map!`, that injects `k` (and `v` for objects) into the computational context.

```
w> map! { 0 5 1 4 2 3 } {k (? k.< 1 k.+ v $)}
{ 2 5 }
```

The `omap` and `omap!` variants of `map` take a `set` to an `object`.

```
w> omap! int { k k.+ 1 } 5
6
```

## `set`

As mentioned, there are several useful predefined sets that ship with Wall: `int`, `float`, `bool`, `complex`, `string`, `symbol`, and `object` are several of them.

There are two ways to check if a `thing` belongs to a `set`.

```
w> [].in? set
true
w> set? []
true
w> in? 1.0 float
true
w> 1.0.float?
true
```

## ordered things

There is no predefined way to create ordered things in Wall. You can, however, create an object that functions like an array in languages like JavaScript.

```
w> a = { 0 5 1 2 2 6 }
w> a 0
5
w> a 1
2
```

It is also possible to create linked lists.

```
w> ; = 
w> z = omap! thing @ { c $%% ; } { k (z .& { ; { a c } } ) } .& { ; {} }
w> z ;
{}
w> z 1 2 3 ;
{ 1 { 2 { 3 {} } } }
w> q = z 1 2 3 4
w> q 5 ;
{ 1 { 2 { 3 { 4 { 5 {} } } } } }
```

This works because Wall's evaluation is lazy, meaning that it only fetches information on a need-to-know basis.  By the time that `z` has been constructed, the top-level object has a key-value pair `{ ; {} }`, which means that `c` will evaluate to `{}`. Then, because everything in Wall is a copy, the inside `z` is a copy of the original `z` with the `;` key set to `{ a {} }`.  For those of you familiar with Scheme, this is not unlike how a list is constructed: `(cons 1 (cons 2 '()))` is the list `'(1 2)`.