# Guards II

We've already seen several guards in Wall and seen how they can be used to construct a function with `fun` and `fun!`.  In this section, we will see some more strategies on how to build guards.

## Rolling your own guards

Remembering `<5?` from the first guard section, we can write this function several ways.

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

We could have written our guard like this as well.

```
w> <5? = fmap! everything (? (int? k) (< k 5) false)
w> another<5? = f+ (fmap everything false) (fmap! int (< k 5))
w> == <5? another<5?
true
```

Yet another strategy is to use the `?ify` function, which creates a guard from a set that should validate positively.

```
w> <5? = fmap! everything (? (int? k) (< k 5) false)
w> yet-another<5? = ?ify (filt! int (> 5))
w> == <5? yet-another<5?
true
```

## Using your own guards

You can use your own guards the same way you'd use a pre-defined guard in any Wall function defined by `fun` or `fun!`.

```
w> <5? = ?ify (filt! int (> 5))
w> foo = fun [_? <5?] (? (> a1 3) 0 a0)
w> foo 'hello -1
'hello
w> foo {} 4
0
w> foo {} 10
Error. The function `foo {}` does not contain the value `10` in its domain.
```

## Strategies for making guards

There are two common strategies to make a guard:

- Create a set of elements that are valid and call `?ify` on that set.
- Define a function that yields an object mapping all elements to either `true` or `false`.
 
### `?ify` strategy

The example below shows two guards defined with the `?fy` strategy.

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

The example below shows the same two guards defined using `fun`.

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

## Predefined guards

Wall ships with hundreds of predefined guards that end with `?` *and* functions that work on guards that end with `??`.  The latter functions combine the results of guards - for example `|??` applies the `|` operation to the result of two guards.

Here are some, just as a taste of what is possible:

| Function        | Validates                                         |
| --------------- | ------------------------------------------------- |
| `int?`          | Is this an integer?                               |
| `->? x y`       | Is this a function that takes `x` and returns `y` |
| `list?`         | Is this a list?                                   |
| `inside? x`     | Is x inside this?                                 |
| `<? x`          | Is this less than x?                              | 