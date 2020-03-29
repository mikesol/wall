# Functions IV

This section will teach you how to define functions with `fun`.

## `fun`

`fun` takes two arguments: a list of sets and an expression.  It uses the sets to construct the domain of the function, and uses the expression to construct the range.  Internally, `fun` calls `bind` on the expression to bind it to its arguments. For more on bind, see [Percent](./syntax-2#perent).

```
w> anything-or-0 = fun [_ int] (? (> %k 5) 0 %%k)
w> anything-or-0 'hello 6
'hello
w> anything-or-0 'hello 5
0
w> hello-or-0 = anything-or-0 'hello
w> hello-or-0 6
'hello
```

Recalling from the [Percent](./syntax-2#percent) section, `%k` refers to one level up in a function heirarchy and `%%k` represents to two levels up.  In pseudocode, we could say that `foo` is constructed like so:

```
foo = {
  <element of _>: {
    <element of int>: bind (? (> %k 5) 0 %%k)
  }
}
```

With this representation, and following the syntax presented in [Percent](./syntax-2#percent) it is more clear that `%k` represents `<element of int>` and `%%k` represents `<element of _>`.
