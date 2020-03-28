# Sets II

Wall has lots of predefined sets.  Some of them resemble types in other languages, like `int`, `string`, `symbol` and `complex`. In Wall, `int` is the set of all integers, `string` is the set of all strings, `symbol` is the set of all symbols and `complex` is the set of all complex numbers.

```
w> int .== (s+e int 0)
true
w> string .== (s+e string 0)
false
w> foo =
w> symbol foo
true
w> subs? int complex
true
```

## `everything`

There is one special set called `everything` that contains everything that Wall does or will ever contain, including itself.

```
w> int.subs? everything
true
w> everything.s- everything
:[]
w> everything.subs? everything
true
```