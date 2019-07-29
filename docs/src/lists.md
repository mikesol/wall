 # Lists

Lists are built using square brackets.

```
w> first second =
w> [ first second ]
[ first second ]
w> []
[]
```

Lists support indexing by placing an integer after the list.

```
w> a b =
w> [a b] 0
a
```

Wall will throw a compile-time error if a list cannot be indexed either because the index is out of bounds or the size of the list is unknown.