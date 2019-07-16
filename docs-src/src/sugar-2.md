# Sugar II

More sugar!!!

## Pattern matching

What would a functional language be without pattern matching?  Pattern matching works in assignment or in `@` blocks.  Patterns are always functions that map value names to operations on the object on the right that would yield that value.

```
w> { 'a id 'b id } = { 'a 0 'b 1 }
w> a
0
w> b
1
```

Note that pattern matching only works on parts of values that have no ambiguity.  If an object is created conditionally based on a random value or IO operation, pattern matching will only work on the part of the object that is non-random.

## The `!` family

We've seen functions like `map` and `red`, but they have much more usable variants called `map!` and `red!` that use `@` under the hood to create some yummy named things.

```
w> min0x = map! int \ k $? k .$> 0 0 k
w> min0x 4
4
w> min0x -1
0
```

Under the hood, `map!` injects a variable `k` into the local context using `@` under the hood.  Its cousin, `map!!`, does the same thing for functions, automatically applying `id` (the identity function) to anything that is not a pair and otherwise injecting `k` and `v` for the key and value, respectively.

```
w> map!! [ \ 0 1 \ 2 3 \ 4 5 ] \ k (+ v 7)
[ \ 0 8 \ 2 10 \4 12 ]
```

The same is true of `red` - `red!` injects the accumulator `a` and the key `k`, while `red!!` throws in v for good measure.

```
w> red! [1 2 3] (+ a (* 2 k)) 0
12
w> red!! [ \ 0 1 \ 2 3 ] (s+ [ \ k (+ k v ) ]) []
[ \ 0 1 \ 2 5 ]
```

## Namespace conflicts

As mentioned, Wall does not allow for two elements to have the same name in the same scope *or* in nested scopes.  This poses a challenge if we want to nest maps.  To get around it, we have the following (very lazy) functions for *map* and *red* that create different variable names.

```
w> foo = [ \ 0 [ \ 1 2 ] ]
w> map!!a-b foo [ \ a.+ 1 (map!!c-d b [ \ (c.+ 2) (d.+ 3) ]) ]
[ \ 1 [ \ 3 5 ] ]
```