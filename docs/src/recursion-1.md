# [Recursion I](/recursion-1)

In Wall, any named element can refer to itself in its definition.

```
w> z = \ 6 z
w> car z
6
```

Wall does its best to handle most recursive structures, but some are too difficult for it to stomach.  For example, Wall is not smart enough (yet) to evaluate the following code and will throw an error.  Don't worry that you haven't seen `map!` yet - it just maps a set to another set.

```
w> z = map! int ? k.== 15 k (z ? k.> 15 k.- 1 k.+ 1)
w> q = map! int 15
w> == z q
Error. Relationship between the objects is unknown.
```

A lot of pre-defined functions in Wall are defined using recursion.  For example, we have been creating lists in a rather annoying way so far by using the `\` function successively.  Wouldn't it be nice if we could create a list with a syntax like, for example, `\( 1 2 3 4 )\`?  Recursion to the rescue!

