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

## Coq

Wall uses [Coq](https://coq.inria.fr) in order to construct all of its proofs. There are two major axioms that Wall adds on top of Coq in order to construct programs. While a detailed discussion of both axioms is outside the scope of this guide, we will describe them briefly here, focusing on how they pertain to Wall.

### Extentionality

The [Axiom of Extentionality](https://en.wikipedia.org/wiki/Axiom_of_extensionality) states that if two sets have all the same members, then they are the same set. Wall applies this axiom to all possible values (numbers, sets, functions). So, even if two functions have different definitions, if their domain is equivalent to their range, then they are the same.

```
== (fmap! everything (id a0)) (fmap! everything (id id a0))
true
```

### Axiom of choice

Informally, the axiom of choice says that if we have a non-empty set, we can choose an arbitrary value from that non-empty set. This is what allows the function `choose` to be possible in Wall for *any* set.