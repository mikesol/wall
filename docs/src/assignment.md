# Assignment

Assignment in Wall is accomplished with the equal sign.  Technically, all the symbols we have seen so far are assignments in that they are assigned to names that refer to themselves.  Any valid unicode sequence can be used as a name in Wall, provided that it has not been previously used by the language itself or an imported module.

```
w> apple =
w> banana =
w> pear =
w> fruit = [ apple banana pear ]
w> fruit
[ apple banana pear ]
```

Assignment in wall is immutable, meaning that once something has been asigned to a name, the name will refer to that thing for the duration of a program.

```
w> stacy = []
w> stacy = [[]]
Error. `stacy` cannot be reassigned.
```