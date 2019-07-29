# [Recursion](/recursion)

In Wall, any function can refer to itself in its definition.

```
w> z = fun [int?] ? (<= a0 1) 1 (* a0 (z (- a0 1)))
w> z 5
120
```

Under the hood, Wall does its best to handle most recursive functions, but some are too difficult for it to stomach.  For example, Wall is not smart enough (yet) to evaluate the following code and will throw an error.

```
w> z = fmap! int ? k.== 15 k (z ? k.> 15 k.- 1 k.+ 1)
w> q = fmap! int 15
w> == z q // This is true, but Wall doesn't know that (yet).
Error. Relationship between the objects is unknown.
```

In these (rare) cases, there are two options.  One is to use the `@[depth default]` symbol after the function to indicate a recursion depth and a default argument to return in case the depth is hit.  This will unfold the function `depth` times and return `default` if that depth is hit.

```
w> z = fmap! int ? k.== 15 k (z@[100 15] ? k.> 15 k.- 1 k.+ 1)
w> q = fmap! int 15
w> == z q
true
```

Another option is to use the `ter` function. `ter`, for tail-end recursion, accepts three functions: one that acts as a gate to continue or not, one that represents the value to return if the gate is false, and one that represents the argument applied to the function if the gate is true.

```
w> z = (ter
    (<< 1 (== a0 []))
    (<< 1 a0)
    (<< 1 (? (list? a0) (cdr a0) [])))
w> z [1 2 3 4 5]
[]
```

The disadvantage of `ter` is that the range is overly large compared to the actual range of the function.  This is because its range is inferred only from the second argument that represents the function's termination.

```
w> z = (ter
    (<< 1 (== a0 []))
    (<< 1 a0)
    (<< 1 (? (list? a0) (cdr a0) [])))
w> == everything (ran z)
true
w> q = (ter
    (<< 1 (== a0 []))
    (<< 1 (? (list? a0) a0 []))
    (<< 1 (? (list? a0) (cdr a0) [])))
w> == list (ran q)
true
```

In spite of this limitation, `ter` is an effective, if not verbose, method to hack around compilation errors from recursive functions.