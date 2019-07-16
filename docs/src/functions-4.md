# Functions IV

Some functions in Wall mimic control structures in imperative languages: constructors, loops, etc.  Here, we see the three most common "control" functions in Wall: `flip`, `map` and `red`.

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

## `map`

`map` maps values from a set to another set.  To remind you of the various ways we can express map using parentheses and dots, check out the equivalent examples below.

```
w> map [1 2 3] (+ 3)
[4 5 6]
w> [1 2 3].map (+ 3)
[4 5 6]
w> [1 2 3].map 3.+
[4 5 6]
w> [1 2 3].map 0.*
[0]
```

A variant of map, `map:` also works on lists.  Recall that there is no primitive type for a list, so we use duck typing to represent a pair whose second element is either a pair or something else, terminating at "something else".  `map:` takes that "something else" as its first argument and then works as expected.

```
; =
w> map: ; ( \ 1 ( \ 2 ; )) 3.+
\; 4 5 ;\
```

A built-in version of `map` exists for the `()` symbol.

```
w> map:() ( \ 1 ( \ 2 () )) 3.+
\() 1 2 ()\
```

## `red`

`red` is used to perform a reduction over a set. The penultimate argument is a transitive function that takes two arguments: the aggregator and the next value.  The final argument is an initial value to serve as the aggregator.

```
w> red [1 2 3] + 0
6
w> red [[1 2] [2 3] [3]] s+ []
[1 2 3]
```

If the function is not transitive, Wall will throw an error.

```
w> red { 1 2 1 3 1 5 } f+e []
Error. The function `red [\ 1 2 \ 1 3 \ 1 5]` does not `f+e` in its domain.
```

When `red:` and `red:()` are used, the transitivity is not needed as the order of evaluation is known.
