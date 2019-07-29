# Functions II

We have already seen several pre-defined functions in Wall, like `car`, `cdr` etc.  There are many more: `<`, `+`, `cos`, `map`, etc.  Wall pre-defines hundreds of functions in the language that you can use right out of the box.  They are pre-defined for several reasons

- they would be really difficult or bothersome to define; and/or
- the maintainers have an opinionated veiw about how they should be defined; and/or
- they are so common/useful that it is difficult to imagine *not* having them pre-defined.

It is outside the scope of this section to present all of the pre-defined functinos in Wall.  Here, we will just show some popular ones.

## General

`id` is the identity function in Wall.

```
w> id 1
1
```

`just` returns a constant independent of the incoming value.

```
w> just 1 5000
1
w> just 'foo 4999
'foo
```

## Math

Not surprisingly, `+` adds two numbers, `-` subtracts them, `*` multiplies them, and `\` divides them.  `\\` is integer division, `mod` is the modulo operation, and `**` is exponentiation.

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

## Strings

Strings *are* functions in Wall and, as such, can be invoked to yield a value.  Specifically, they can be invoked with an index or set of indices to yield a substirng.

```
w> "abc" 0
"a"
w> "peace" [0 1]
"pe"
w> "שלום" O
"ש"
w> "שלום peace" 0
"ש"
w> "שלום peace" [0 1 2 3 4]
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

## Comparisons

Not surprisingly...

```
w> < 3 4
true
w> < 4 3
false
w> <= 4 4
true
w> == 4 3
false
w> == [1 2] [2 1]
true
```

Ok, the last one may have been a bit surprising.  In Wall, equality means "contains the same stuff."  So if two sets or two pairs have the same stuff, they are equal according to Wall.

## Logic

Also not surprisingly...

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

## Conversion

You can convert basic values like so:

```
w> str2int "5"
5
w> int2real 5
5.0
w> sym2str #hello#
"hello"
```

## Sets

Two sets can be combined using `s+`.  An element can be added to a set using `s+e`.

```
w> s+ [1 2 3] [2 3 4]
[1 2 3 4]
w> s+e [1 2 3] 5
[1 2 3 5]
```

The difference of two sets is `s-`, and an element can be taken from a set using `s-e`. Note that if any elemetn from the stuff to be taken away is not present in the original set, an error will be thrown.

```
w> s- [1 2 3] [2 3]
[1]
w> s-e [1 2 3] 1
[2 3]
w> s- [1 2 3] [3 4]
Error. The function `s- [1 2 3]` does not contain the element `[3 4]` in its domain.
```

Set inclusion can be tested with `in?`, and subset-itude can be tested with `subs?`.

```
w> in? 1 [1 2 3 4]
true
w> subs? [1] [1 2 3 4]
true
```

## Lists

You can use `car` and `cdr` to get the head and tail of a list.

```
w> car \ 6 3
6
w> cdr \ 6 3
3
```



## Functions

Similar functions `f+` and `f-` exist for functions.

```
w> f+e { 1 2 3 4 } { 5 6 7 8 }
{ 1 2 3 4 5 6 7 8 }
w> f+e { 1 2 3 4 } { 3 5 7 8 }
{ 1 2 3 5 7 8 }
w> f- { 1 2 3 4 } 1
{ 3 4 }
```

And who could forget classics like `dom`, which returns a function's domain, and `ran`, which returns its range?

```
w> dom { 1 2 3 4 }
[ 1 2 ]
w> ran { 1 2 3 4 }
[ 3 4 ]
```

Lastly, while we invoke functions using a syntax `foo 1`, we can also invoke them using the function `invoke`:

```
w> { 1 2 3 4 } 1
1
w> invoke  { 1 2 3 4 } 1
1
```