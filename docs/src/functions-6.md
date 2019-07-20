# Functions VI

In the last section, we saw that `int?` is a validator.  We saw that `<5?` is also a validator.  Both are functions that map all possible objects to either `true` or `false`.

We have also seen that functins defined with ``<<>>`` take a validator and use it to construct the domain of the function.  For example:

```
w> foo = <<! int? >> a0 + 1
w> == int (dom foo)
true
```

So, what if we construct a similar function with `<5?`?  Let's see:

```
w> <5? = <<n 1 (& (int? a0) (< a0 5))
w> foo = <<! <5? >> a0 + 1
w> == int (dom foo)
false
w> == (filt! int (>= 5)) (dom foo)
true
```

Some languages call this "dependent typing", but in Wall, it's just constructing functions with different domains.