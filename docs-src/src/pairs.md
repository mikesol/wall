 
# Pairs

Pairs in Wall, like in Scheme, represent an ordered pair.  They are built using backslash followed by two elements.

```
w> first =
w> second =
w> \ first second
\ first second
```

Like in Scheme, you can use `car` and `cdr` to get the first and second element of a pair respectively.  `car` and `cdr` are both [Functions](/functions) (as are `\` and `[`), so we are jumping the gun a bit to talk about them, but hey, you're smart, so you probably will grok how they work by checking out the example below.

```
w> car \ 6 3
6
w> cdr \ 6 3
3
```
