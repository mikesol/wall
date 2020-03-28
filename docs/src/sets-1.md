# Sets I

Wa are constructed with square brackets preceded by a colon. Elements are separated by one or more whitespaces.  Sets can contain anything in Wall.  Since we have already seen symbols, we'll use some for demonstration purposes.

```
w> apple banana pear =
w> :[ apple banana pear ]
:[ apple banana pear ]
```

Sets are just functions whose domain contains all valid Wall values and whose range contains `true` and `false`. All elements present in the set produce `true`, and all elements not present in the set produce `false`. Thus, the following code is valid Wall syntax.

```
w> apple banana pear =
w> basket = :[ apple banana ]
w> basket apple
true
w> basket pear
false
```