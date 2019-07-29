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
w> baz =
w> #foo bar#
foo bar
w> baz
baz
```

The code above creates two symbols: `foo bar` and `baz`.  In instances where a symbol has whitespace, the `#` character is used to preserve whitespace.  To use a `#` in a symbol, you can escape it with `\`.  The end of the symbol and the `=` sign must be separated by at least 1 whitespace.

Multiple symbols can be declared by separating them with whitespace.

```
w> foo bar baz =
w> foo
foo
w> bar
bar
w> baz
baz
```

Symbols are useful in Wall in that they are guaranteed to only exist in Wall.  That is, they are native to Wall and can never be imported from some other format like JSON or YAML, nor can they be exported to another format.

Of course, you can't do much useful stuff with symbols aside from print "Hello, world!" to the command line.  In the next section, we'll see how sets offer a slight improvement.
