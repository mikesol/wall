# Functions I

Functions in Wall are represented in curly brackets and represent key-value pairs.  Each pair is separated by a space, as are the elements within each pair.  Functions are roughly equivalent to `dict` in Python and `Object` in JavaScript, with the important caveat that they can have infinitely-large domains.

```
w> Paris France Berlin Germany =
w> { Paris France Berlin Germany }
{ Paris France Berlin Germany }
```

## Invocation

Of course, functions are no fun unless you can invoke them with an argument to yield a result.  In Wall, this is done simply by separating the function and its argument with whitespace.

```
w> Paris France Berlin Germany =
w> { Paris France Berlin Germany } Paris
France
```

## Errors

Wall will issue a compile-time error if a function cannot be evaluated because it lacks (or might lack) the required element in its domain.

```
w> Paris France Berlin Germany Budapest =
w> { Paris France Berlin Germany } Budapest
Error. The function `{ Paris France Berlin Germany }` does not contain `Budapest` in its domain.
```

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

## You'll be seeing a lot of these

Functions are the only data structure available in Wall. They is inspired by [Lua's tables](https://www.lua.org/pil/2.5.html), which are Lua's only data structure.  That means that, when we see [Sets](./sets-1) and [Lists](./lists-1) later on, they will also be functions.