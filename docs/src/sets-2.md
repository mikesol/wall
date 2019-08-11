# Sets II

Wall has lots of predefined sets.  For example, every primitive type in Wall is just set, so we can do stuff like:

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
:[]
w> everything.subs? everything
true
```

## `choose`

Remember that in [Functions II](./functions-2#sets), we mentioned that that Wall is not smart enough to know the cardinality of sets.  It *can*, however, verify that a set `s` is non-empty by checking `== s :[]`.

A function `choose` is defined in all non-empty sets that can choose a random value from them. The kicker is that *you cannot know what this value is*. That may seem a bit artificial. For example, `choose :[1]` can only ever return `1`, but Wall will only represent the outcome of this function invocation as "a random choice from `:[1]`."