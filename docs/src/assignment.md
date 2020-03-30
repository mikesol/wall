# Assignment

Assignment in Wall is accomplished with the equal sign.  Any valid [Symbol](./symbols) can be used for an assignment in Wall.

```
w> apple banana pear =
w> fruit = apple
w> fruit
apple
w> #My favorite fruit!# = pear
w> #My favorite fruit!#
pear
```


Assignment in wall is immutable, meaning that once something has been asigned to a name, the name will refer to that thing for the duration of a program.

```
w> stacy fred = 
w> stacy = fred
CannotReassignError. `stacy` cannot be reassigned.
```
