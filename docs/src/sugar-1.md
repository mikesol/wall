# Sugar I

Like lots of other languages, Wall has some delicious morcels of syntactic sugar that make it a little easier to read and write code.

## `\`

You've likely run into the scenario before where you create a string and assign it to the same name as the string.

```
w> FOOBAR = "FOOBAR"
```

In Wall, you can accomplish the same thing using the `\` morcel:

```
w> \ FOOBAR
w> FOOBAR
"FOOBAR"
w> \ #DELICIOUSLY LONG#
w> #DELICIOUSLY LONG#
"DELICIOUSLY LONG"
```

## `%`

Sometimes, when working with "container" primitive types like sets and pairs, it is useful to refer to elements higher up in the heirarchy.  One way to do this is to manually create these references.

```
w> #one level back# =
w> c = [ \ 'level 'c ]
w> b = [ \ 'level 'b \ 'next & [ \ #one level back# b ] c ]
w> a = [ \ 'level 'a \ 'next & [ \ #one level back# a ] b ]
w> #b up# = b #one level back#
w> == #b up# a
true
w> lr = \
```

## `@`

Sometimes, you need to give something a name only in a limited context and then have the name evaporate.  In Haskell, this is accomplished with `let`.  In Wall, this is accomplished with `@`.  `@` accepts a function with *only* symbols in the domain (it will complain otherwise) and has access to all elements in the current *and* outer scopes.