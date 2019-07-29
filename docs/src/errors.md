 # Errors

Now that you've learned the basics in Wall, you can already to a fair bit of exploring.  While exploring, if you're anything like everyone else, you will surely run into errors.  We've already seen a few already, but just for fun, let's create some more!

```
w> 1 2
Error. `1` is not a function.
w> { 2 3 } 4
Error. The function `{ 2 3 }` does not contain the element `4` in its domain.
```

One of Wall's killer features is that it only throws *compile-time errors*.  That is, once Wall is up and running, you can be sure that the only reason a Wall program will ever crash is if there is a bug in Wall.

This doesn't just work for simple functions like `{ 2 3 }`.  Remember how the function `red` needs a transitive function as its second argument?

```
w> red { 1 2 1 3 1 5 } f+e []
Error. The function `red { 1 2 1 3 1 5 }` does not contain `f+e` in its domain.
```

Wall is smart enough, at compile time, to know that `f+e` is *not* a transitive function.  That's pretty darn cool.  So while you may hit a lot of errors in the Wall interpreter or when invoking the While compiler, rest assured that, an error-free compiled Wall program is one of the safest things you can push to production.

The rest of this section will guide you in a more nuanced exploration of Wall.  By the end, you should be able to write simple yet powerful Wall programs.