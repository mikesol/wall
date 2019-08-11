# Proofs

As previously mentioned, Wall keeps track of the properties of all values in the current scope. For example, if `c = 5`, then `c` has the property of being equal to five at compilation time, and at runtime, c *is* five.

Internally, every property about a Wall value is used to prove theorems. Theorems are only ever about function invocation and are in the form *"If A and B and C, then there exists an x such that x = D and x is in the domain of f."* Naturally, *A*, *B*, and *C* need to say something meaningful about both *D* and *f* for a proof to be constructed. Proofs that are not verifiably true underlie every compilation error in Wall.

## Coq

Wall uses [Coq](https://coq.inria.fr) in order to construct all of its proofs. There are two major axioms that Wall adds on top of Coq in order to construct programs. While a detailed discussion of both axioms is outside the scope of this guide, we will describe them briefly here, focusing on how they pertain to Wall.

### Axiom of Extentionality

The [Axiom of Extentionality](https://en.wikipedia.org/wiki/Axiom_of_extensionality) states that if two sets have all the same members, then they are the same set. Wall applies this axiom to all possible values (numbers, sets, functions). So, even if two functions have different definitions, if their domain is equivalent to their range, then they are the same.

```
== (fmap! everything (id a0)) (fmap! everything (id id a0))
true
```

### Axiom of Choice

Informally, the [Axiom of Choice](https://en.wikipedia.org/wiki/Axiom_of_choice) says that if we have a non-empty set, we can choose an arbitrary value from that non-empty set. This is what allows the function `choose` to be possible in Wall for *any* set.

While we can choose a value from any set, because it is impossible to know *which* element it is, we can never remove that element from the set. Counterintuitively, this is even the case in sets that only contain one element. One way to think of this is that while sets contain specific elements, `choice` removes the element's specificity and assigns to it only properties. Thus, even if we are sure that a set `s` contains only one element and that `choice s` will surely choose *that* element, we cannot go backwards from the *non-specific* chosen element to the *specific* element in the set because `choice` erases that element's specificity.