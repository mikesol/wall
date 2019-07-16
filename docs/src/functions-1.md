# Functions I

There is no inherent representation of functions in Wall.  There is, however, a convention that will allow us to build things that function like, well, functions.

A function is a set containing at least one pair where no two pairs have the same `first` element.  This is kind of like the mathematical definition of a function with the important distinction that Wall will still consider a set a function even if it contains elements that are not ordered pairs, so long as no two pairs have the same first element.  Thus, the last two lines below are both functions.

```
w> Paris France Berlin Germany =
w> #Capitals to Countries# =
w> [ \ Paris France \ Berlin Germany ]
w> [ #Capitals to Countries# \ Paris France \ Berlin Germany ]
```

## Invocation

Of course, functions are no fun unless you can invoke them with an argument to yield a result.  In Wall, this is done simply by separating the function and its argument with whitespace.

```
w> Paris France Berlin Germany =
w> [ \ Paris France \ Berlin Germany ] Paris
France
```

## Errors

Wall will issue a compile-time error if a function cannot be evaluated because it lacks (or might lack) the required element in its domain.

```
w> Paris France Berlin Germany Budapest =
w> [ \ Paris France \ Berlin Germany ] Budapest
Error. The function `[ \ Paris France \ Berlin Germany ]` does not contain `Budapest` in its domain.
```

Also, if you try to invoke something that is not a function like a function, it will complain.

```
w> Paris=
w> France=
w> France Paris
Error. `France` is not a function.
```

## `{}`

A common shorthand for function creation in Wall is `{ 1 2 3 4 }` instead of `[ \ 1 2 \ 3 4 ]`.  When possible, functions are printed using the `{}` syntax.

## Currying

There is no such thing in Wall as a function with more than one argument.  Like in Haskell, all functions take one argument.  They can, however, yield functions as values.  This is commonly called *Currying*, named after Haskell Curry.

```
w> Left Right Up Down =
w> FinalDirection = {
    Left { Right Up Left Down }
    Right { Left Up Right Down }
}
w> FinalDirection Right Left
Up
```

## Objects

In Wall, there are no "objects".  However, it is sometimes useful to refer to a function as an object.  You can of course call them whatever you'd like, but the important bit to remember is that they are a set of ordered pairs where no two first elements are the same.