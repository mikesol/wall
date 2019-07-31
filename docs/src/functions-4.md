# Functions IV

Somtimes, you would like to define your own functions over an infinite domain, like all integers.  We have already seen a way to do this using `fmap`.

```
w> +' = fmap!a int (fmap!b int (+ a b))
w> == + +'
true
```

The same can be accomplished using validators using `fun` and `fun!`.

## `fun` and `fun!`

`fun` takes two arguments: a list of validators and any expression, and returns a nested function mapping the first domain to the second domain, the second domain to the third domain, etc. until it reaches the range, which is just the expression supplied to `fun` or `fun!`.  Under the hood, both `fun` and `fun!` use `@{}` to inject locally-scoped named values into the computational context.

In the case of `fun`, values named `a0, a1, ... aN` are injected into the context, where `N` is the length of the incoming list.

```
w> foo = fun [_? int?] ? $> a1 5 0 a0
w> foo {} 6
{}
w> foo {} 5
0
```

`foo` is a function that takes two arguments, where the first can be anything and the second must be an integer. It returns `0` if the second argument is greater than `5`, else it returns the first argument.

Sometimes, it is useful to work with named arguments.  There is a version of `fun` called `fun!` that does this.

```
w> foo = fun! ['baz _? 'bar int?] ? $> bar 5 0 baz
w> foo {} 6
{}
w> foo {} 5
0
```

For the supremely lazy, there is `<< n` that takes `n` arguments whose validator is `_?`.

```
w> foo = << 2 (fmap! ($? (set? a0) a0 [a0]) (== a1 k))
w> foo [1 2 3] 2
{ 1 false 2 true 3 false }
w> foo true true
{ true true }
```
