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

Lists are just functions containing contiguous integers in the range starting from 0. Thus, the following two structures are identical:

```
w> a b =
w> [a b]
[a b]
w> { 0: a, 1: b }
[a b]
```