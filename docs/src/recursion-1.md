# [Recursion I](/recursion-1)

In Wall, any named element can refer to itself in its definition.

```
w> z = \ 6 z
w> car z
6
```

Recursion in Wall is just a form of syntactic sugar that expands a function 16 times and, if the function does not terminate before expansion ends, returns the special symbol `wall`.  You can override both of these by using the `@(terminal, numtimes)` operator after the symbol being recursed over.

```
w> z = \ 'a z
w> cdr z
\ 'a $\ 'a $\ 'a $\ 'a $\ 'a $\ 'a $\ 'a $\ 'a ... \$ wall
w> cadddr z
'a
w> a = \ 6 a @(5, 'b)
\ 'a $\ 'a $\ 'a $\ 'a $\ 'a 'b
```

Note that the recursive function cannot be called directly or indirectly from the `@` function.

A lot of pre-defined functions in Wall are defined using recursion.  For example, we have been creating lists in a rather annoying way so far by using the `\` function successively.  Wouldn't it be nice if we could create a list with a syntax like, for example, `\( 1 2 3 4 )\`?  Recursion to the rescue!

