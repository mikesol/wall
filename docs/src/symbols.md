# Symbols

Let's revisit "Hello, world!" in Wall.

```
w> #Hello, world!# =
w> #Hello, world!#
Hello, world!
```

In this bit of code, we have actually created a symbol called `Hello, world!`. Symbols in Wall are created in the following manner:

```
w> #foo bar# =
w> #foo bar#
#foo bar#
w> baz =
w> baz
baz
```

The code above creates two symbols: `foo bar` and `baz`.  In instances where a symbol has non-alphanumeric characters, the `#` character must bookend the symbol.  To use a `#` in a symbol, you can escape it with `\`.  The end of the symbol and the `=` sign must be separated by at least 1 whitespace.

Multiple symbols can be declared by separating them with whitespace and appending the equals sign to the end of the declaration.

```
w> foo bar baz =
w> foo
foo
w> bar
bar
w> baz
baz
```

Symbols are conceptually similar to [*atoms* in Erlang](http://erlang.org/doc/reference_manual/data_types.html#atom).
