# Functions III

Let's dive a bit deeper into function invocation in Wall.

## Greed

By default, all function invocations in Wall are maximally *greedy*.  That is, when invoked, they will gobble any argument, even if it is a function.  Sometimes, this is what we want.

```
w> name = [ \ > "greater than" \ < "less than" ]
w> name <
"less than"
```

However, sometimes, we don't want this at all.  Consider the following case:

```
w> Dad Sister Brother Son Daughter Roberto Miguel Betty =
w> Relation = [
  \ Roberto [ \ Miguel Dad \ Anita Dad ]
  \ Miguel [ \ Anita Brother \ Roberto Son ]
  \ Anita [ \ Miguel Sister \ Roberto Daughter ]
]
w> Role = [
  \ Brother Miguel
  \ Sister Anita
  \ Dad Roberto
  \ Daughter Anita
  \ Son Miguel
]
w> Relation Role Dad Roberto
Error. The function `Relation` does not contain an element `Role` in its domain. 
```

Intuitively, we are trying to get whoever plays the `Role` of `Dad` and figure out what he is to `Roberto`.  But so far, we have seen no way to do this.  Instead, because `Relation` is greedy, it will try to look for `Role` in its domain and, predictably, fail.

## Parentheses

In order to fix this greedy problem, Wall (like lots of other languages) uses parentheses to signal "evaluate whatever is inside here before moving onto the outer context."  Let's revisit the `size` example above, but use parentheses to make it work.

```
w> Dad Sister Brother Son Daughter Roberto Miguel Betty =
w> Relation = [
  \ Roberto [ \ Miguel Dad \ Anita Dad ]
  \ Miguel [ \ Anita Brother \ Roberto Son ]
  \ Anita [ \ Miguel Sister \ Roberto Daughter ]
]
w> Role = [
  \ Brother Miguel
  \ Sister Anita
  \ Dad Roberto
  \ Daughter Anita
  \ Son Miguel
]
w> Relation (Role Dad) Roberto
Dad
```

Here, the parentheses say to Wall "hey, forget about that greedy `Relation` for a second. Let's figure out what's inside here first, and then we'll feed it to the `Relation`."

## Dots

The `.` symbol in Wall does two things.  It *flips* function invocation so that what comes *after* the period calls whatever comes before the period, and it automatically adds parentheses around the next two elements.  Whitespace is optional both before and after the dot.

```
w> Dad Sister Brother Son Daughter Roberto Miguel Betty =
w> Relation = [
  \ Roberto [ \ Miguel Dad \ Anita Dad ]
  \ Miguel [ \ Anita Brother \ Roberto Son ]
  \ Anita [ \ Miguel Sister \ Roberto Daughter ]
]
w> Role = [
  \ Brother Miguel
  \ Sister Anita
  \ Dad Roberto
  \ Daughter Anita
  \ Son Miguel
]
w> Relation Miguel Anita
Brother
w> Miguel.Relation Anita
Brother
```

This is why it is not a good idea to use `.` in variable names in Wall.  While technically allowed, it nullifies `.` syntax wherever it is used.

```
w> Dad Sister Brother Son Daughter Roberto Miguel Betty =
w> Relation = [
  \ Roberto [ \ Miguel Dad \ Anita Dad ]
  \ Miguel [ \ Anita Brother \ Roberto Son ]
  \ Anita [ \ Miguel Sister \ Roberto Daughter ]
]
w> my.symbol =
w> my = Miguel
w> symbol = Relation
w> my.symbol Anita
Error. `my.symbol` is not a function.
```

## Dollars

It is fitting that, when talking about a greedy protocol, we conclude with a discussion of the `$` sign.  `$` in Wall has a special meaning like `$`.  It means "put parentheses around whatever comes after me until there are no more functions to invoke".

```
w> \ 1 (\ 2 (\ 3 4))
\ 1 (\ 2 (\ 3 4))
w> \ 1 $ \ 2 $ \ 3 4
\ 1 (\ 2 (\ 3 4))
w> foo = \ 1 $ \ 2 $ \ 3
w> foo 4
\ 1 (\ 2 (\ 3 4))
```

## Dotted dollars

Lastly, the `.$` symbol works like `.` *except* that, instead of putting parentheses around the elements before and after the dot, it puts parentheses around the element after the dot and everything that follows, like `$`.

```
w> 6 .$\ 5 .$\ 4 3
(\ 6 (\ 5 (\ 4 3)))
```