# Validation II

We've already seen several validators in Wall and seen how they can be used to construct functions with `<<`.  In this section, we will see some more strategies on how to build validators.

## Rolling your own validators

We can write our own validators:

```
w> <5? = <<! _? >> (& (int? a0) (< a0 5))
w> <5? 4
true
w> <5? 5
false
w> 5?
```

We could have written our validator like this as well.

```
w> <5? = s+ (map! everything [ \ k false ]) (map! int [ \ k (< k 5) ])
```

The pattern in this example is common in Wall. Take a union of two functions, where:

- one function maps everything to false
- one function maps the values in the positive set to true

This pattern can also be accomplished using the `?ify` object, which creates a validator from a set that should validate positively.

```
w> <5? = ?ify (filt! int (> 5))
```

Now, let's rewrite `foo` from above using a custom validator:

```
w> <5? = ?ify (filt! int (> 5))
w> foo = def! 'a0 _? 'a1 <5? fed (? (> a1 3) 0 a0)
w> foo 'hello -1
'hello
w> foo {} 4
0
w> foo {} 10
Error. The key 10 does not exist on the object `foo` {}. 
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
 
### `<<!` strategy

```
w> a0? = <<! 'a _? >> { a (a == { a' 0 }) }
w> a0? { 'a 0 }
true
w> a0? 0
false
w> n_n+1? = <<! 'a _? >> { a (== (a 'n+1) (+ 1 (a 'n))) }
w> n_n+1? { 'n 0 'n+1 1 }
true
w> n_n+1? { 'n 0 'n+1 2 }
false
w> n_n+1? 0
false
```

## Validating recursive `object`-s

You may remember that a the constructor of a linked list can be defined like so.

```
w> () bar =
w> foo = map! everything (flip \ (s+ foo [ \ bar (\ k ((%% bar)))])) .s+ [ \ bar ()]
```

This is one of many ways to define a link list's constructor, and intuitively, we may want to ask "is an object a linked list according to this definition"?

One way to do this is to use `?ify` on the values of the aggregator keys `bar` that exist on the recursive versions of `z`.  Another way to do this is to create a validator describing the list's properties.  The results will be the same.

```
w> () bar =
w> foo = map! everything (flip \ (s+ foo [ \ bar (\ k ((%% bar)))])) .s+ [ \ bar ()]
w> ll1 = (<<! (ify? [foo]) >> ([a0 bar] .s+ (red (map (dom (f- a0 bar) ll1) s+)))) foo
w> ll1? = ?ify ll1
w> ll1? (foo 3 2 1 bar)
true
w> ll1? (\ 1 $\ 2 $\ 3 ())
true
ww> ll1? (\ 1 $\ 2 3)
false
w> ll2? = <<n 1 (| (== a0 ()) ((pair? a0) & (ll2 (cdr a0))))
w> ll2? (\ 1 $\ 2 $\ 3 ())
true
w> == ll1? ll2?
true
```

The strategy used for `ll1?` is so useful that there is a prepackaged object called `rag` that does exactly this.  `rag` is short for "reverse aggregator".  It reinforces a common pattern in Wall: define a recursive function constructor with a symbol that acts as an aggregator, and then use `rag` to define the set of objects that the aggregator can hold.


```
w> () bar =
w> foo = map! everything (flip \ (s+ foo [ \ bar (\ k ((%% bar)))])) .s+ [ \ bar ()]
w> ll1 = rag foo bar
w> ll1? = ?ify ll1
w> ll2? = <<n 1 (| (== a0 ()) ((pair? a0) & (ll2 (cdr a0))))
w> == ll1? ll2?
true
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