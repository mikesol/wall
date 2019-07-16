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

## coqi

When Wall invokes its compiler, the first thing it does is transpiles Wall code to `coq`.  Then, it uses `coqi`, a brute-force theorem prover, to prove the integrity of the program.  `coqi` maintains a database of proven theorems to speed up the compilation process when online.

While `coqi` can brute-force its way through most proofs that anyone would need in a real-world application, there are certain corner cases that are difficult for it to handle, mostly having to do with infinite series and recursion.  In this case, Wall will throw a compilation error that it cannot *proove* a program to be correct.