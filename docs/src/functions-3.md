# Functions III

Some functions in Wall mimic control structures in imperative languages: constructors, loops, etc.  Here, we see the four most common "control" functions in Wall: `flip`, `filt`, `map` and `red`.

## `flip`

Flip takes three arguments: a function and two arguments (call them `a` and `b` to that function).  It then invokes the function with `b` followed by `a` instead of `a` and then `b`.  For example, we can define a mirror function to `>=` called `>='` using flip.

```
w> >=' = flip <
w> >=' 4 3
true
w> >=' 4 4
true
w> >=' 4 5
false
w> == >=' >=
true
```

## `filt`

`filt` filters a list or set:

```
w> filt [1 2 3 4] (< 2)
[3 4]
```

## `map`

`map` maps values from a list, set or function to another list, set or function.  To remind you of the various ways we can express map using parentheses and dots, check out the equivalent examples below.

```
w> map [1 2 3] (+ 3)
[4 5 6]
w> [1 2 3].map (+ 3)
[4 5 6]
w> [1 2 3].map (* 0)
[0 0 0]
w> :[1 2 3].map (* 0)
[0]
w> {1: 2, 3: 4, 5: 6}.map (* 0)
{ 1: 0, 3: 0, 5: 0 }
```

A cousing of `map`, called `fmap`, maps a set, list, or function to a function.

```
w> fmap [1 2 3] (* 3)
{ 1: 3, 2: 6, 3: 9 }
w> fmap :[1 2 3] (* 3)
{ 1: 3, 2: 6, 3: 9 }
w> fmap { 'a: 1, 'b: 2, 'c: 3 } (* 3)
{ 'a: 3, 'b: 6, 'c: 9 }
```

There is also a function `xmap` that works like `fmap` but is applied to the function's keys. `xmap` needs to be an injunctive function, otherwise the compiler will throw an error.

```
w> xmap { 1: 2, 3: 4 } (* 3)
{ 3: 2, 9: 4 }
w> xmap { 1: 2, 3: 4 } (* 0)
Error. The function `xmap { 1: 2, 3: 4 }` does not contain `(* 0)` in its domain.
```

## `red`

`red` is used to perform a reduction over a list. The penultimate argument is a function that takes two arguments: the aggregator and the next value.  The final argument is an initial value to serve as the aggregator.

```
w> red [1 2 3] + 0
6
```

Importantly, `red` cannot be performed on a set.