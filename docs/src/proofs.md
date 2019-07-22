# Proofs

So let's say we have the following Wall session.

```
w> g = <<! (<? 2) >> + a0 1
w> y = rand0 ; .* 5
w> z = rand0 ; .* 2
w> g z
1.734243
w> g y
Error. The function `g` may not contain key `y`.
```

This works as expected, but how does Wall know that `g` should fail when `y` is applied?  The intuitive answer is "because Wall knows that `rand0` returns a value between 0 and 1, so y is between 0 and 5, so it may be greater than 2 and thus g cannot ingest it."  But how do we *know* that there exists a number between 0 and 5 such that the number does not exist in the set of numbers between 0 and 2.  Well, we have to proove it.

## Z3

When Wall invokes its compiler, the first thing it does is invokes the [Z3](https://github.com/Z3Prover/z3) SMT prover to prove the correctness of the program.