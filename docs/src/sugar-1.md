# Sugar I

Like lots of other languages, Wall has some delicious morcels of syntactic sugar that make it a little easier to read and write code.  We have already seen two of them: `.` and `$`.  In editors, sugar is colored differently, and sugar can *never* be interpreted as symbols or named values.  That means that you can't do something like:

```
w> [ $ . ]
Error. Cannot understand how to use `$`.
Error. Cannot understand how to use `.`.
```

## String constants

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

## Percent

Sometimes, when working with functions, it is useful to refer to elements higher up in the function's heirarchy.  One way to do this is to manually create these references.

```
w> #one level back# =
w> c = { 'level 'c }
w> b = { 'level 'b 'next $& { #one level back# b } c }
w> a = { 'level 'a 'next $& { #one level back# a } b }
w> #b up# = b #one level back#
w> == #b up# a
true
```

Wall provides the family of `%` commands to make this sort of manipulation a bit easier.

- `%` the current function
- `%k` the key pointing to the current value

Adding percent signs increases how far in the heirarchy we go.  So, for example, `%%` is the previous function, `%%k` is the key pointing to the key pointing to the current value, etc.

Sometimes, you want to refer to other bits of a function's *original* enclosure.  To do this, we use the same convention as above, but ending with an exclamation point:

- `%!`: the *original* current function
- `%k` the *original* key pointing to the current value

```
w> a = { 'a { %k %% 'b } 'b 1 }
w> b = { 'a { %k! %%! 'b } 'b 1 }
w> a 'a
{ 'a 1 }
w> b 'a
{ 'a 1 }
w> c = { 'q (a 'a) 'b 3 }
w> d = { 'q (b 'a) 'b 3 }
w> c 'q
{ 'q 3 }
w> d 'q
{ 'a 1 }
```

Because the un-exclamationed form of `%k`, `%%` etc resolves to *any* enclosing element, there will be no compiler error until you attempt to *access* an object with `%k`, `%%` etc.

```
w> a = { %k %%k }
w> b = { %k! %%k! }
Error. %% b is not a function.
w> c = { 0 a }
w> d = { 0 { 1 a } }
w> d 0 1
{ 1 0 }
w> c 0
Error. %% c is not a function. 
```

## Ampersand

Sometimes, you need to give something a name only in a limited context and then have the name evaporate.  In Haskell, this is accomplished with `let`.  In Wall, this is accomplished with `@`.  `@` accepts a function with *only* strings in the domain (it will complain otherwise) and has access to all elements in the current *and* outer scopes.


```
w> @ { 'a 3 'b 2 } { a b b a }
{ 3 2 2 3 }
```

By default `@` do not accumulate, meaning that only the values from the final `@` are useable in the object.  To force an `@` to persist, use `@>`.  To pull in the values from a prior at, use `>@`.  To exclude values from an `@`, use `~`.

```
w> @ { 'a { 'c 3 } 'b 2 } >@ { 'c (a 'c) } { b c c a }
{ 3 2 2 { 'c 3 } }
w> @> { 'a { 'c 3 } 'b 2 } @ { 'c (a 'c) } { b c c a }
{ 3 2 2 { 'c 3 } }
```

Anything in `@` cannot conflict with a toplevel name *or* a name in a lower scope.  So the compiler will raise an error for something like this:

```
w> @ { 'a 1 'b 2 } { @ { 'a 1 'b 2 } a a b b }
Error. Cannot reassign `a`.
```

`@` can also come *after* a named `object`, in which case it will persist to *any* time the named `object` is used.

```
w> b = { 1 0 } @ { 'a 1 }
w> b a
3
```

In editors like VS Code, you can always see the currently defined names in the Wall inspector and their scopes.
