# Syntax I

Wall has some syntactic shortcuts that make it a little easier to read and write code.

## Parentheses

By default, all function invocations in Wall are *greedy*.  That is, when invoked, they will try to gobble any value to their right. However, sometimes, we don't want this at all.  Consider the following case:

```
w> == == 3 4 == 4 5
Error. `false` is not a function.
```

Intuitively, we would like to ask "Is 3 == 4 equal to 4 == 5?".  We can do this with parentheses.  Let's revisit the `==` example above, but use parentheses to make it work.

```
w> == (== 3 4) (== 4 5)
true
```

Here, the expressions within parentheses (`== 3 4)` and `(== 4 5)`) are evaluated before the outermost expression.


## Dots

The `.` symbol in Wall *flips* function invocation so that what comes *after* the period calls whatever comes before the period.  Whitespace is optional both before and after the dot.

```
w> (3 .== 4) .== (4 .== 5)
```

The dot syntax allows anything in Wall to become an infix operator, which makes it look and feel a bit more like Python or JavaScript.

## Dollars

`$` in Wall means "suspend the current stack and open a new one until there is no function on the new stack anymore *or* until there is a newline".

```
w> ? false 0 $? false 1 $? true 2 $? false 3 4
2
```

## Dotted dollars

Lastly, the `.$` sign combines `.` and `$`.

```
w> 6 .$- 5 .$- 4 .- 3
2
w> == (6 .$- 5 .$- 4 .- 3) (- 6 (- 5 (- 4 3)))
true
w> 6 .- 5 .- 4 .- 3
-6
w> == (6 .- 5 .- 4 .- 3) (- (- (- 6 5) 4) 3)
true
```
