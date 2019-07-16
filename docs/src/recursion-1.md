# [Recursion I](/recursion-1)

In Wall, any named element can refer to itself in its definition.  Because it evaluates lazily, it will only ever throw an error if it is asked to perform an IO operation using a recursive (or infinite) structure as an argument.  Otherwise, the recursive element is useable anywhere it's needed.

```
w> z = \ 6 z
w> car z
6
w> cdr z
Error. IO operation using the recursive element `z`.
w> cadr z
6
w> cadddr z
6
```

A lot of pre-defined functions in Wall are defined using recursion.  For example, we have been creating lists in a rather annoying way so far by using the `\` function successively.  Wouldn't it be nice if we could create a list with a syntax like, for example, `\( 1 2 3 4 )\`?  Recursion to the rescue!

