# Sugar I

Like lots of other languages, Wall has some delicious morcels of syntactic sugar that make it a little easier to read and write code.

## `\ STRING`

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
w> b = [ \ 'level 'b \ 'next $& [ \ #one level back# b ] c ]
w> a = [ \ 'level 'a \ 'next $& [ \ #one level back# a ] b ]
w> #b up# = b #one level back#
w> == #b up# a
true
w> lr = \ 'foo (car lr)
w> cdr lr
'foo
```

Wall provides the family of `%` commands that are references to other bits of structures to make this sort of manipulation a bit easier.

- `%` the innermost enclosing set to which an element belongs
- `%k` the innermost `first` value of an enclosing pair to which an element belongs
- `%v` the innermost `second` value of an enclosing pair to which an element belongs

Adding percent signs increases how far in the heirarchy we go.

Sometimes, you want to refer to other bits of an `object`-s *original* enclosing set or pair.  To do this, we use the same convention as above, but ending with an exclamation point:

- `%!`: the *original* innermost enclosing set to which an element belongs
- `%k` the *original* innermost `first` value of an enclosing pair to which an element belongs
- `%v` the *original* innermost `second` value of an enclosing pair to which an element belongs

```
w> a = [ \ 'a [ \ %k %% %k ] ]
w> b = [ \ 'a [ \ %k! %%! %k! ] ]
w> a 'a
[ \ 'a ' a ]
w> b 'a
[ \ 'a 'a ]
w> c = [ \ 'q a 'a ]
w> d = [ \ 'q b 'a ]
w> c q'
\ 'q 'q
w> d q'
\ 'a 'a
```

Because the un-exclamationed form of `%k`, `%%` etc resolves to *any* enclosing element, there will be no compiler error until you attempt to *access* an object with `%k`, `%%` etc.

```
w> a = [ \ %k %%k ]
w> b = [ \ %k! %%k! ]
Error. %% b is not a function.
w> c = [ \ 0 a ]
w> d = [ \ 0 [ \ 1 a ] ]
w> d 0 1
\ 1 0
w> c 0
Error. %% c is not a function. 
```

## `@`

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
