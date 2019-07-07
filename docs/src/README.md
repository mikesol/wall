# Wall

This is the documentation for the Wall programming language.

[[toc]]

## Things

Wall has five predefined sets: `int`, `float`, `bool`, 'symbol', and `object`.  The union of these five sets along with the set of all sets is called a `thing`.  Here is how we can learn the set to which a `thing` belongs in Wall.
```

w> :s 1
int
w> :s 'a'
char
w> :s { 'a 1 }
object
```

And here's how we can verify the set to which something belongs as a boolean:

```
w> float? 1.0
true
w> float? 1
false
w> set? [1]
true
w> list? 1
false
```

Any `thing` can be given a name in Wall. Named things are immutable, meaning once they are created, they cannot be changed. Names in Wall cannot be `$` or `@`, start with a number or `.`, and cannot contain whitespace. Otherwise, the world's your oyster!

```
w> anne = 1
w> anne = 2
Error. Cannot reassign `anne`.
w> things_to_do = ["eat", "sleep"]
w> things_to_do 0 = "drink"
Error. Cannot reassign `things_to_do` 0.
w> &!-@\./ = "a very strange name"
w> &!-@\./
"a very strange name"
```

In this section, we will explore the five basic sets.  Objects, as they are so important in Wall, will get a little extra love.

### `int`

In Wall, `int` represents and integer (surprise!). Integers in Wall are unbounded, which means they can be as big or tiny as you'd like to be. Groups of three digits can be separated by an underscore (`_`).

```
w> 5
5
w> 0
0
w> -1
-1
w> -0
0
w> 1_000_000_000
1_000_000_000
w> -999999
-999_999
```

### `float`

Floats are represented as double-precision floating numbers in Wall. They function like an `int`. A `float` can be added to an `int`, at which point the result is a float.

```
w> 5.1
5.1
w> 0.0
0.0
w> -1.3
-1.3
w> -1_000_000_000.000000
1_000_000_000.0
w> -999999.0013000
-999_999.0013
w> + 1 3.0
4.0
```

### `bool`

Like in other languages, a `bool` can be `true` or `false`.

```
w> a = true
w> b = false
w> is? a b
false
```

### `symbol`

A symbol is created the same way that a variable is, except no right-hand part is given.

```
w> a =
w> b =
w> c = a
w> a
a
w> c
a
w> b
b
```

Symbols do not seem that useful for now, but we will see a few, like `$`, that are really important.  Basically, symbols are useful as keys in objects that can be differentiated from all other keys and given special values.

### `object`

An object in Wall is just a collection of keys and values, where keys can be any `thing` and values can as well. While an object can have the same value for several different keys, the reverse is not true - keys in Wall, like in most languages, can only have one value.

```
w> a = { 'a 1 'b 2 }
w> b = { 'b 3 'c 4 }
w> & a b
{ 'a 1 'b 3 'c 4 }
```

A value can be retreived from an object using the following convention:

```
w> a = { 0 1 'b 2 }
w> b = { 5 3 'c 4 }
w> a 'b
2
w> (& a b) 5
3
```

Sometimes, when constructing or destructuring an object, it's useful to refer to other bits of the object. You can do that with the following conventions:

- `.`: the present object.
- `.k`: the key that points to this object in the enclosing object.
- `..`: the enclosing object
- `...k`: the key that points to the enclosing object.

...and so forth and so on.

Furthermore, the special Wall-defined symbol `$` in objects means "ignore my key" when used as a value.  It can be used as a key like any other symbol.

```
w> a = { 'a { 'b { 'c { 'd { 'e .......k 'f (.. 'g) 'h $ } 'g 1 } } } }
w> a
{ 'a { 'b { 'c { 'd { 'e 'a 'f 1 } 'f 1 } } } }
w> is? (a 'a ..) a
true
w> is? { 'a $ 'b $ } {}
true
```

Wall will throw an error if you create an object that is infinitely recursive.

```
w> { 'a . }
Error. Recursive object definition.
w> { 'a 0 'b { 'a (+ 1 (.. 'a)) 'b (? (< (. 'a) 2) . $) } }
{ 'a 0 'b 'a 1 'b { 'a 2 } } }
```

One last bit of syntactic sugar is `@`. `@`, like `let` in Haskell, can be used to create local named things in a context that are *only* valid in that context. `@` takes an object whose keys are valid names. There can be as many `@`-s as one likes before the object, but they do not accumulate, meaning that only the values from the final `@` are useable in the object.

```
w> { @ { 'a 1 'b 2 } a a b b }
{ 1 1 2 2 }
```

### `set`

A set in Wall is a collection of **unordered** items.

```
w> [1 2 3]
[1 2 3]
w> in? 1 [1 2 3]
true
```

The special element `$` works similar as in an `object` - it is ignored.

```
w> [1 2 $]
[1 2]
w> [1 2] & [$]
[1 2]
w> len [1 $]
1
```

## Predefined things

Some `thing`-s in Wall are predefined. That is, they are defined by the Wall maintainers for you.  They are predefined for several reasons:

- they would be really difficult or bothersome to define; and/or
- the maintainers have an opinionated veiw about how they should be defined.

For example, think about the following object:

```
w> < = { 0 { 1 true } 1 { 2 true 0 false } }
w> < 0 1
true
w> < 1 0
false
w> < 1 2
true
```

This object works very much like the relation `<`, or less-than. `0` is less than `1`, `1` is not less than `0`, etc. However, this object would become difficult to manually define for every imaginable integer.  Indeed, it would be impossible. That's why Wall has predefined `object`-s and, more generally, predefined `thing`-s.

### `float`

Wall comes with a few predefined `float`-s that are sometimes useful.

```
w> rand
0.055325461
w> now
1562524244.200712
```

Because Wall evaluates lazily, these objects will evaluate only when they need to. To force evaluation, you can use the `!` variants of both.

```
w> rand!
0.055325461
w> now!
1562524244.200712
```
### `object`

Wall has lots of predefined objects, and lots of syntactic sugar to work with or create these objects.

#### Strings

In Wall, Strings are objects that can be created three different ways:

```
w> a = 'aString
w> print a
aString
w> b = "a\tString"
w> print b
a    String
w> c = `${a}
${b}`
w> print c
aString
a    String
```

Strings can be manipulated fairly easily using standard conventions:

```
w> "abc"
"abc"
w> string? "abc"
true
w> substr "abc" 0
"a"
w> substr "peace" (range 0 2)
"pe"
w> substr "שלום" O
"ש"
w> substr "שלום peace" 0
"ש"
w> substr "שלום peace" (range 0 5)
"שלום p"
w> substr "שלום peace" 5
"ש"
```

Wall has a fun bit of syntactic sugar for named strings. Instead of writing:

```
w> HELLO = "HELLO"
w> HELLO
"HELLO"
```

We can just write:

```
w> \HELLO
w> HELLO
"HELLO"
```

#### `f`

`f` is a predefined object that, intuitively, describes something that resembles a function in other languages. As a convention, all function names should end with `$`.

```
w> foo$ = f _? int? $ @ { a0 ...k a1 .k } ? (> a1 5) 0 a0
w> foo$ {} 6
{}
w> foo$ {} 5
{}
```

In other languages, we would say something like:

> `foo$` is a function that takes two arguments, where the first can be anything and the second must be an integer. It returns `0` if the second argument is greater than `5`, else it returns the first argument.

In Wall, we'd say:

> `foo$` is a nested object. `k` can be anything. `v.k` must be an integer. And `v.v` is `0` or `k` depending if `v.k` is greater than `5`.

#### `r`

Sometimes, you want to reduce the key/value pairs in an `object` or `set`, like summing them up. That's done with `r`.

```
w> r [1 2 3] + 0
6
w> r [{'a 1} {'b 2} {'c 3}] & {}
{'a 1 'b 2 'c 3}
w> r { 0 5 1 4 2 3 } @ { k ...k v .k } (& {k (? (< k 1) (+ k v) $)}) {}
{ 2 5 }
w> r [8 3 2] @ { k .k } (& (? (< k 4) (+ k 3) 0)) []
[11 0 0]
```

### ordered things

There is no predefined way to create ordered things in Wall. You can, however, create an object that functions like an array in languages like JavaScript.

```
w> a = { 0 5 1 2 2 6 }
w> a 0
5
w> a 1
2
```

### `set`

As mentioned, there are five predefined sets: `int`, `float`, `char`, `bool`, 'symbol', and `object`.  There are two ways to check if a `thing` belongs to a `set`.

```
w> in? [] set
true
w> set? []
true
w> in? 1.0 float
true
w> float? 1.0
true
```