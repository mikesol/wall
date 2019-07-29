 # Errors

Now that you've learned the basics in Wall, you can already to a fair bit of exploring.  While exploring, if you're anything like everyone else, you will surely run into errors.  We've already seen a few already, but just for fun, let's create some more!

```
w> 1 2
Error. `1` is not a function.
w> { 2 3 } 4
Error. The function `{ 2 3 }` does not contain the element `4` in its domain.
```

One of Wall's killer features is that it only throws *compile-time errors*.  That is, once Wall is up and running, you can be sure that the only reason a Wall program will ever crash is if there is a bug in Wall.
