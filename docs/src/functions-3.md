# Functions III

Let's dive a bit deeper into function composition and invocation in Wall.

## `{}`

A common shorthand for function creation in Wall is `{ 1 2 3 4 }` instead of `[ \ 1 2 \ 3 4 ]`.  When possible, functions are printed using the `{}` syntax.

## Greed

By default, all function invocations in Wall are maximally *greedy*.  That is, when invoked, they will gobble any argument that may be in their domain, even if it is a function.  Sometimes, this is what we want.

```
w> name = [ \ > "greater than" \ < "less than" ]
w> name <
"less than"
```

This also provides a sensible default for lots of cases where writing parentheses is annoying.  For example:

```
w> + + 5 3 1
9
```

As `+ is not in the domain of `+`, `+` ignores it and waits until a value in its domain shows up.  If nothing comes before a newline, it will raise an error.

However, sometimes, we don't want this at all.  Consider the following case:

```
w> == == 3 4 == 4 5
Error. `false` is not a function.
```

Intuitively, we would like to ask "Is 3 == 4 equal to 4 == 5?".  We can do this with parentheses.

## Parentheses

In order to fix this greedy problem, Wall (like lots of other languages) uses parentheses to signal "evaluate whatever is inside here before moving onto the outer context."  Let's revisit the `==` example above, but use parentheses to make it work.

```
w> == (== 3 4) (== 4 5)
true
```

Here, the parentheses say to Wall "hey, forget about that greedy `==` for a second. Let's figure out what's inside here first, and then we'll feed it to the `==`."

## Dots

The `.` symbol in Wall *flips* function invocation so that what comes *after* the period calls whatever comes before the period.  Whitespace is optional both before and after the dot.

```
w> (3 .== 4) .== (4 .== 5)
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

It is fitting that, when talking about a greedy protocol, we conclude with a discussion of the `$` sign.  `$` in Wall means "suspend the current stack and open a new one until there is no function on the new stack anymore".

```
w> \ 1 (\ 2 (\ 3 4))
\ 1 (\ 2 (\ 3 4))
w> \ 1 $ \ 2 $ \ 3 4
\ 1 (\ 2 (\ 3 4))
w> foo = \ 1 $ \ 2 $ \ 3
w> foo 4
\ 1 (\ 2 (\ 3 4))
w> ? false 0 $? false 1 $? true 2 $? false 3 4
2
```

## Dotted dollars

Lastly, the `.$` sign combines `.` and `$` into one uber sign.

```
w> 6 .$\ 5 .$\ 4 3
(\ 6 (\ 5 (\ 4 3)))
```

## 