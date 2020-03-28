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

`filt` filters a list or funtion based on a predicate applied to the values:

```
w> filt [1 2 3 4] (< 2)
[3 4]
w> filt {55: 1, 63: 2, 77: 3, 89: 4} (< 2)
{77: 3, 89: 4}
```

A version for sets, `filt-s`, applies a predicate to values in a set.

```
w> filt-s :[1 2 3 4] (< 2)
:[3 4]
```

## `map`

`map` maps values from a list, set or function to another list, set or function.

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

A version for sets, `map-s`, applies a mapping function to values in a set.

```
w> map-s :[1 2 3 4] (+ 1)
:[2 3 4 5]
```


## `red`

`red` is used to perform a reduction over a function:

- the first argument is the function;
- the second argument is a sorting function for values in he first argument;
- the third argument is a function that acts on the aggregator and the next value; and
- the final argument is an initial value to serve as the aggregator.

```
w> red [1 2 3] < + 0
6
```