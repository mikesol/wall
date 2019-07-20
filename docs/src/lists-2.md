# Lists II

Wall has lots of helper functions to construct lists.  In fact, a Wall program is itself a list (Wall is, after all, a dialect of Lisp).

## `listify`

`listify` takes a terminating character (usually a symbol) and creates a function that will create a list when it encounters the terminal character.

```
w> foobar =
w> end-at-foobar = listify foobar
w> end-at-foobar 1 2 3 foobar
\( 1 2 3 )\
```

## `list`

`list` is just defined as `listify ;`.

```
w> a = list 1 2 3 4 ;
\( 1 2 3 4 )\
```

## `listify` functions are greedy

Because listify functions are greedy, they eat everything except `(`, `)`, `{`, `}`, `[`, and `]`.  That means that `list map int neg` will create a three-element list containing `map`, `int` and `neg`.  To invoke map in the previous example, use `list (map int neg)`.

## Nested lists

`listify` functions keep track internally of the number of times they encounter themselves in order to handle nested lists.  If they do encounter themselves, they create a nested list.

```
w> a = list 1 2 3 list 4 5 6 ; 7 8 9 ;
\( 1 2 3 \( 4 5 6 )\ 7 8 9 )\
```

## `listify!!!`

The function `listify!!!` works like `listify` with one important exception - it is defined on the range of `evverrrythinggg` instead of just `everything`. This means that it will treat `(`, `)`, `{`, `}`, `[`, and `]` as tokens.  Use this with extreme caution, as it is entirely possible to do something like this...

```
w> :_-( =
w> bad = listify!!! :_-(
w> bad (+ 1 2 :_-(
/( ( + 1 2 )/
```

## `list!!!`

`list!!!` is like `list` except defined using `listify!!!`

```
w> len list (+ 1 2) 3 ;
2
w> len list!!! (+ 1 2) 3 ;
6
```

In the above example, the length of our second list is 6 because it treats `(` as a function `)` as a symbol, which means that everything between `(` and `)` is also part of the list.