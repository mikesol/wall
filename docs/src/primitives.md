 # Primitive Types

When we learned about functions in Wall, we learned about structures that *represented* functions.  This is traditionally called *duck-typing* in programming: if it quacks like a duck and walks like a duck, it's a duck.  Wall will consider something that satisfies the conditions of a function a function.

However, we've already seen certain primitive types in Wall like sets, pairs, and symbols that fall outside of this duck-typing scheme.  That is, they are what they are, and nothing else can be them but them.  A combinations of sets and pairs cannot be made to resemble a symbol.  Only a symbol is a symbol.

In addition to sets and pairs, there are three primitive types in Wall that you will use in almost every program --- numbers, strings, and booleans.  While they could also be represented via duck-typing (as could pairs), it is not commonly useful to work with numbers using a representation of numbers.  When we want `1`, it's nice to be able to type `1` and know that nothing else (ie `[[]]` in Zemelo-Frankel set theory) is 1.
