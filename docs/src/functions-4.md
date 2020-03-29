# Functions IV

This section will teach you how to define your own functions over large domains.

## `fun` and `fun!`

`fun` takes two arguments: a list of sets and any expression.  It uses the sets to construct the domain of the (nested) function(s), and uses the expression to construct the range.

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
w> foo :[1 2 3] 2
{ 1: false, 2: true, 3: false }
w> foo true true
{ true: true }
w> (foo int 2) 3
false
```
