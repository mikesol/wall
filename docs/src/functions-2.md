# Functions II

Wall predefines hundreds of functions in the language that you can use right out of the box.  They are predefined for several reasons

- they would be really difficult or bothersome to define; and/or
- the maintainers have an opinionated veiw about how they should be defined; and/or
- they are so common/useful that it is difficult to imagine *not* having them pre-defined.

It is outside the scope of this section to present all of the pre-defined functions in Wall.  Here, we will just show some popular ones.

- [General](#general)
- [Math](#math)
- [Numeric comparisons](#numeric-comparisons)
- [Boolean logic](#boolean-logic)
- [Strings](#strings)
- [Coercion](#coercion)
- [Lists](#lists)
- [Sets](#sets)
- [Functions](#functions)

## General

`id` is the identity function in Wall.

```
w> id 1
1
```

`always` returns a constant independent of the incoming value.

```
w> always 1 5000
1
w> always-hello = always 'hello
w> always-hello 4999
'always-hello
```

`==` represents equality between two values.

```
w> == 1 2
false
w> c = 2
w> == { 1: 2 } { 1: c }
true
w> == just id
false
w> == id id
true
```

## Math

`+` adds two numbers, `-` subtracts them, `*` multiplies them, and `\` divides them.  `\\` is integer division, `mod` is the modulo operation, and `**` is exponentiation.

```
w> + 1 2
3
w> + 4.1 2
6.1
w> + 4-1j 1.1j
4+0.1j
w> - 3 2
1
w> * 3 7
21
w> / 3 2
1.5
w> // 7 2
3
w> mod 10 3
1
w> ** 4 0.5
2.0
```

All common trigonometric functions are defined in Wall, as is the constant `pi`.  Because `pi` is so commonly used, one can omit the multiplication sign when working with it (like `j` for complex numbers).

```
w> sin 2pi
0
w> cos pi
-1
w> tan 0
0
w> csc 0.5pi
1
w> sec 0
1
w> cot 0.25pi
1
w> arcsin 0
0
```

Logarithmic functions are defined along with `e`, which works like `pi` and `j`.

```
w> ln e
1
w> log 10 100
2
```

## Numeric comparisons

Here are some classic numeric comparisons, like less than and greater than, implemented in wall.

```
w> < 3 4
true
w> > 3 4
false
w> <= 4 4
true
```

## Boolean logic

Here are some boolean operators in Wall.

```
w> & true false
false
w> | true false
true
w> x| false false
true
w> -> true false
false
w> <-> true true
true
w> ? true 0 1
0
```

## Strings

Strings act like lists in Wall and, as such, can be invoked to yield a value.  Specifically, they can be invoked with an index or list of indices to yield a substirng.

```
w> "abc" 0
"a"
w> "peace" [0 1]
"pe"
w> "שלום" O
"ש"
w> "שלום peace" 0
"ש"
w> "שלום peace" [0 1: 2, 3: 4]
"שלום p"
w> "שלום peace" 5
"ש"
```

Strings can also be manipulated with lots of builtin functions, including full regex support.

```
w> ++ "Hello, " "world!"
"Hello, world!"
w> split "has spaces" " " 0
"has"
w> re:match '123 "123 foo bar" 0
"123"
```

## Coercion

You can coerce certain primitive types to other primitive types like so:

```
w> str2int "5"
5
w> str2bytes "hello"
b"hello"
w> int2real 5
5.0
w> sym2str #hello#
"hello"
```

## Lists

You can use `head` and `tail` to get the head and tail of a list.

```
w> head [ 6 4 3 ]
6
w> tail [ 6 4 3 ]
[4 3]
```

`reverse` reverses a list and `concat` concatenates two lists.

```
w> reverse [1 2 3]
[ 3 2 1 ]
w> concat [1 2 3] [4 5 6]
[ 1: 2, 3: 4 5 6 ]
w> len [1 2 3]
3
```

## Sets

Two sets can be combined using `s+`.  An element can be added to a set using `s+e`.

```
w> s+ :[1 2 3] :[2 3 4]
:[ 1 2 3 4 ]
w> s+e :[1 2 3] 5
:[ 1 2 3 5 ]
```

The difference of two sets is `s-`, and an element can be taken from a set using `s-e`.

```
w> s- :[1 2 3] :[2 3]
:[ 1 ]
w> s-e :[1 2 3] 1
:[ 2 3 ]
w> s- :[1 2 3] :[3 4]
:[ 1 2 ]
```

Testing for inclusion in a set is done by invoking the set with a value (as the set is just a function). Testing if a subset is in a set can be achieved with `subs?`.

```
w> :[1 2 3 4] 1
true
w> subs? :[1] :[1 2 3 4]
true
```

A set can be transformed to a function that keeps only those values that evaluate to `true` by using `keep`.

```
w> int 'hello
false
w> (keep int) 5
true
w> (keep int) 'hello
IncorrectDomainError. The function `(keep int)` does not or may not contain the element `'hello` in its domain.
```

## Functions

Just as sets above have `s+`, `s-` and `s-e`, functions have `f+`, `f-`, and `f-e`.

```
w> f+ { 1: 2, 3: 4 } { 5: 6, 7: 8 }
{ 1: 2, 3: 4, 5: 6, 7: 8 }
w> f+ { 1: 2, 3: 4 } { 3: 5, 7: 8 }
{ 1: 2, 3: 5, 7: 8 }
w> f-e { 1: 2, 3: 4 } 1
{ 3: 4 }
w> f- { 1: 2, 3: 4 } :[1 3]
{}
```

Furthermore, `dom` returns a function's domain, and `ran` returns its range.

```
w> dom { 1: 2, 3: 4 }
[ 1 2 ]
w> ran { 1: 2, 3: 4 }
[ 3 4 ]
```

Lastly, while we invoke functions using a syntax `my-function 1`, we can also invoke them using the function `invoke`.

```
w> { 1: 2, 3: 4 } 1
1
w> invoke  { 1: 2, 3: 4 } 1
1
```
