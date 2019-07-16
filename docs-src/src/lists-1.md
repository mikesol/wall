# Lists I

Wall does not have a built-in notion of a list.  A list-like structure can be created, however, by using nested pairs like in Scheme.  Let's use the symbol `()` to represent the end of a list, and then we can use nested pairs to represent a list.

```
w> () =
w> list = 6 .$\ 5 .$\ 4 .$\ 3 .$\ 2 .$\ 1 .$\ 0 ()
w> list
\() 6 5 4 3 2 1 ()\
```

As you can see above, lists print to the console using the pretty syntax of the pair function followed by the list termination symbol to start the list, and the reverse to end it.

We've already seen a glimpse of functions, so let's check out what the function `reverse` does on a list.

```
w> () =
w> list = 6 .$\ 5 .$\ 4 .$\ 3 .$\ 2 .$\ 1 .$\ 0 ()
w> reverse list
\() 6 5 4 3 2 1 ()\
```