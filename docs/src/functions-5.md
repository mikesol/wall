# Functions V

In the last section, we saw that `int?` is a validator.  We saw that `<5?` is also a validator.  Both are functions that map all possible objects to either `true` or `false`.

We have also seen that functins defined with `fun` take a validator and use it to construct the domain of the function.  For example:

```
w> foo = fun [int?] a0 + 1
w> == int (dom foo)
true
```

So, what if we construct a similar function with `<5?`?  Let's see:

```
w> <5? = << 1 (& (int? a0) (< a0 5))
w> foo = fun [<5?] a0 + 1
w> == int (dom foo)
false
w> == (filt! int (>= 5)) (dom foo)
true
```

Custom validators also enforce compile-time errors for invalid input.

```
w> <5? = ?ify (filt! int (> 5))
w> foo = fun [_? <5?] (? (> a1 3) 0 a0)
w> foo 'hello -1
'hello
w> foo {} 4
0
w> foo {} 10
Error. The function `foo {}` does not contain the value `10` in its domain.
```
