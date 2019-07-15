# Sets II

Wall has lots of predefined sets that are a lot like predefined functions - they would be way too annoying to define manually.  For example, every primitive type in Wall is just set, so we can do stuff like:

```
w> int .== (s+e int 0)
true
w> string .== (s+e string 0)
false
w> foo =
w> foo.in? symbol
true
w> int.subs? complex
true
```

## `everything`

There is one special set called `everything` that contains everything that Wall does or will ever contain, including itself.

```
w> int.subs? everything
true
w> everything.s- everything
[]
w> everything.subs? everything
true
```