 # Errors

Now that you've learned the basics in Wall, you can already to a fair bit of exploring.  While exploring, if you're anything like everyone else, you will surely run into errors.

The two main errors in Wall are `NotAFunctionError` and `IncorrectDomainError`.

## Not a function

Wall will throw a `NotAFunctionError` if a value that is not a function, or a value that may not be a function, is invoked as a function

```
w> 1 2
NotAFunctionError. `1` is or may not be a function.
w> {1: 2, 3: 4 } 1
2
w> good = (? (< rand 0.5) {1: 2} {1: 42})
w> good 1
42 // also could be 2 depending on the outcome of rand
w> bad = (? (< rand 0.5) {1: 2} 1)
w> bad 1
NotAFunctionError. `bad` is or may not be a function.
```

## Incorrect domain error

An incorrect domain error is raised when a function is called with a value that is or may not be in the domain of the function.

```
w> { 2: 3 } 4
IncorrectDomainError. The function `{ 2: 3 }` does not or may not contain the element `4` in its domain.
w> good = (? (< rand 0.5) {1: 2} {1: 42})
w> good 1
42 // also could be 2 depending on the outcome of rand
w> bad = (? (< rand 0.5) {1: 2} {2 :5})
w> bad 1
IncorrectDomainError. The function `bad` does not or may not contain the element `1` in its domain.
```