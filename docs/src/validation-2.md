# Validation II

We've already seen several validators in Wall and seen how they can be used to construct a function with `fun` and `fun!`.  In this section, we will see some more strategies on how to build validators.

## Rolling your own validators

Remembering `<5?` from the first validator section, we can write this function several ways.

```
w> <5? = fmap! everything (? (int? k) (< k 5) false)
w> also<5? = fun [_?] (& (int? a0) (< a0 5))
w> <5? 4
true
w> also<5? 5
false
w> == <5? also<5?
true
```

We could have written our validator like this as well.

```
w> <5? = fmap! everything (? (int? k) (< k 5) false)
w> another<5? = f+ (fmap everything false) (fmap! int (< k 5))
w> == <5? another<5?
true
```

Yet another strategy is to use the `?ify` function, which creates a validator from a set that should validate positively.

```
w> <5? = fmap! everything (? (int? k) (< k 5) false)
w> yet-another<5? = ?ify (filt! int (> 5))
w> == <5? yet-another<5?
true
```

## Strategies for making validators

There are two common strategies to make a validator:

- Create a set of elements that are valid and call `?ify` on that set.
- Define a function that yields an object mapping all elements to either `true` or `false`.
 
### `?ify` strategy

The example below shows two validators defined with the `?fy` strategy.

```
w> a0? = ?ify :[{ 'a 0 }]
w> a0? { 'a 0 }
true
w> a0? 0
false
w> n_n+1? = ?ify (dom (fun [int?] { 'n a0 'n+1 (+ a0 1) }))
w> n_n+1? { 'n 0 'n+1 1 }
true
w> n_n+1? { 'n 0 'n+1 2 }
false
w> n_n+1? 0
false
```
 
### `fun` strategy

The example below shows the same two validators defined using `fun`.

```
w> a0? = fun [_?] (a0 == { 'a 0 })
w> a0? { 'a 0 }
true
w> a0? 0
false
w> n_n+1? = fun [_?] (
    (fun? a0) .&
    (== :['n 'n+1] (dom a0)) .&
    (== (a0 'n+1) (+ 1 (a0 'n))))
w> n_n+1? { 'n 0 'n+1 1 }
true
w> n_n+1? { 'n 0 'n+1 2 }
false
w> n_n+1? 0
false
```

## Predefined validators

Wall ships with hundreds of predefined validators that end with `?` *and* functions that work on validators that end with `??`.  The latter functions combine the results of validators - for example `|??` applies the `|` operation to the result of two validators.

Here are some, just as a taste of what is possible:

| Function        | Validates                                         |
| --------------- | ------------------------------------------------- |
| `int?`          | Is this an integer?                               |
| `->? x y`       | Is this a function that takes `x` and returns `y` |
| `list?`         | Is this a list?                                   |
| `inside? x`     | Is x inside this?                                 |
| `<? x`          | Is this less than x?                              | 