# Sugar II

More sugar!!!  This time, we'll look at functions that use sugar under the hood to make sweet, sweet syntactic goodness.

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