# Syntax II

Here are some more syntactical conventions in Wall.

## Percent

Functions have a domain and range.  Sometimes, it is useful to refer to a function's domain from its range.  In the case of curried functions, functions are like a heirarchy: a domain links to a domain which eventually links to a range.  Here, it may be useful to refer to higher levels of heirarchy from lower ones.

One way to do this is to manually create these references.  In the following example, we use `next` and `back` to make it possible to navigate through a nested function.

```
w> next back =
w> c = { level: 'c }
w> b = { level: 'b, next: (f+ { back: b } c) }
w> a = { level: 'a, next: (f+ { back: a } b) }
w> a-back = a next back
w> == a-back a
true
```

Wall provides the family of `%` commands to make this sort of manipulation a bit easier.

- `%` the current function
- `%k` the key pointing to the current value

Adding percent signs increases how far back in the heirarchy we go.  So, for example, `%%` is the previous function.

Sometimes, you want to refer to other bits of a function's *original* enclosure.  To do this, we use the same convention as above, but ending with an exclamation point:

- `%!`: the *original* current function
- `%k!` the *original* key pointing to the current value

In the example below, `fun1` and `fun2` start by meaning the same thing. However, `fun3` and `fun4` show how `%` and `%!` lead to different behavior.

```
w> // fun1 = { 'a: { 'a: (fun1 'b) }, 'b: 1 }
w> fun1 = { 'a { %k: (%% 'b) ,} 'b: 1 }
w> // fun2 = { 'a: { 'a: (fun2 'b) }, 'b: 1 }
w> fun2 = { 'a: { %k!: (%%! 'b) }, 'b: 1 }
w> fun1 'a
{ 'a 1 }
w> fun2 'a
{ 'a 1 }
w> // because fun1 uses % instead of %!, when fun3
w> // is defined, a will refer to the structure of
w> // fun3 instead of referring to fun1
w> // fun3 = { 'q: { 'q: (fun3 'b) }, 'b: 3 }
w> fun3 = { 'q: (fun1 'a), 'b: 3 }
w> // fun4, on the other hand, will refer to fun2
w> // because fun2 used %! instead of %
w> // fun4 = { 'q: { 'a: (fun2 'b) }, 'b: 3 }
w> fun4 = { 'q: (fun2 'a), 'b: 3 }
w> fun3 'q
{ 'q: 3 }
w> fun4 'q
{ 'a: 1 }
```

## Ampersand

Sometimes, you need to create an assignment in a local scope that does not persist to the top level.  [In Haskell, this is accomplished with `let`](http://learnyouahaskell.com/syntax-in-functions#let-it-be).  In Wall, this is accomplished with `@`.

`@` accepts a function with *only* symbols in the domain (it won't compile otherwise). Then, it treats domain-range pairs as assignments in the following value.


```
w> @ { x: 3, y: 2 } { a: y, b: x }
{ a: 2, b: 3 }
```

Multiple `@` can be used, and parentheses work the same way as with function evaluation to delimit a scope:

```
w> @ { x: 3} (@ { y: 2 } { a: y, b: x })
{ a: 2, b: 3 }
```

Any assignments in `@` cannot conflict with an assignment in a higher scope.  So the compiler will raise an error for something like this:

```
w> @ { a: 1, b: 2 } @ { a: 1, b: 2 } { a: a, b: b }
CannotReassignError. Cannot reassign `a`.
```
