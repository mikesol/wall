# Assignment

Assignment in Wall is accomplished with the equal sign.  Any valid ASCII sequence can be used as a name in Wall, provided that it is not a number, does not contain ```"`'.```, and does not start with any of these characters: `(){}[]$`.

```
w> apple banana pear =
w> fruit = apple
w> fruit
apple
```

Assignment in wall is immutable, meaning that once something has been asigned to a name, the name will refer to that thing for the duration of a program.

```
w> stacy fred = 
w> stacy = fred
CannotReassignError. `stacy` cannot be reassigned.
```
