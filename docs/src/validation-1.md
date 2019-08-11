# Validation I

Wall's killer feature is validation of input.  For safe code, meaning code that exists only within the walls of Wall, validation is done at compile time. For unsafe code, meaning code that does some form of IO, the same validators that you use for your safe code can easily be used for your unsafe code.  So, conceptually, there is little to no distinction between validating dynamic input (ie the result of an API call) and making sure a function has valid input.

## Properties and validation

The Wall compiler keeps a running tab of the strictest possible properties of each value, named or unnamed.

```
// six-to-seven.wall
c = ? true 5 -3
d = c + 1
six-to-seven = { 6 7 }
+ (six-to-seven d) (six-to-seven c)
```

```
$ wall six-to-seven.wall
Error. The function `{ 6 7 }` does not contain `5` in its domain.
```

It is important to note that the error above is a *compile-time* error, meaning that as you are typing the code in your editor or compiling it, Wall will complain.

This is one of the few times we are showing Wall code outside of the interactive environment, and for good reason. In the Wall interpreter, every bit of code is evaluated when you press `ENTER`.  Thus, `w> ? true 5 -3` will evaluate to 5 immediately. While Wall does not *evaluate* this code at compile time, Wall understands that a *property* of `c` is that it is equal to 5, that a *property* of d is that it is equal to 6, and that `six-to-seven` accepts as an argument any number with the *property* of being equal to six.

While this may seem a bit trivial (we could have just said "we're invoking `six-to-seven` with something obviously in its domain"), it becomes more interesting when we deal with IO, indeterminacy, and/or some esoteric sets/functions.

```
// randy.wall
a = floor (* 5 rand)
b = { 0 1 1 2 2 5 3 100 4 52 } a
c = { 0 1 1 2 2 5 3 100 } a
+ b c
```

```
$ wall randy.wall
Error. The function { 0 1 1 2 2 5 3 100 } may not contain `a` in its domain.
```

Here, `a` has the *property* of being in the set `:[0 1 2 3 4]`. While there does not exist a value with the properties of `a` that is not in the domain of `{ 0 1 1 2 2 5 3 100 4 52 }`, there exists a value with the properties of `a` that is not in the domain of ``{ 0 1 1 2 2 5 3 100 }`: namely, the number four.
