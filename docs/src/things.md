 
# Things

Wall has five predefined sets: `int`, `float`, `bool`, `symbol`, and `object`.  An element belonging to the union of these five sets along with the set of all sets is called a `thing`.  Here is how we can learn the set to which a `thing` belongs in Wall.
```

w> ?is 1
int
w> ?is { 'a 1 }
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

Any `thing` can be given a name in Wall. Named things are immutable, meaning once they are created, they cannot be changed. Names in Wall cannot be `$` or `@`, start with `.`, be in the form of an int, float, or string, and cannot contain whitespace. Otherwise, the world's your oyster! That said, a lot of yummy names like `int` and `red` are gobbled up by predefined objects and sets. Sorry!

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
 
## `int`

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
 
## `float`

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
 
## `bool`

Like in other languages, a `bool` can be `true` or `false`.

```
w> a = true
w> b = false
w> is? a b
false
```
 
## `symbol`

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
 
## `object`

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
w> a 'q
Error. The key 'q does not exist on the object `a`.
```

Sometimes, when constructing or destructuring an object, it's useful to refer to other bits of the object. You can do that with the following conventions:

- `.`: the present object.
- `.k`: the key that points to this object in the enclosing object.
- `..`: the enclosing object
- `...k`: the key that points to the enclosing object.

...and so forth and so on.

Furthermore, the special Wall-defined symbol `$` in objects means "ignore me" when used as a key or value.

```
w> a = { 'a { 'b { 'c { 'd { 'e .......k 'f (.. 'g) 'h $ } 'g 1 } } } }
w> a
{ 'a { 'b { 'c { 'd { 'e 'a 'f 1 } 'f 1 } } } }
w> is? (a 'a ..) a
true
w> is? { 'a $ 'b $ } {}
true
w> is? { $ 0 $ 3 } {}
true
```

One last bit of syntactic sugar is `@`. `@`, like `let` in Haskell, can be used to create local named things in a context that are *only* valid in that context. `@` takes an object whose keys are valid names. There can be as many `@`-s as one likes before the object, but they do not accumulate, meaning that only the values from the final `@` are useable in the object.

```
w> @ { 'a 1 'b 2 } { a a b b }
{ 1 1 2 2 }
```

Anything in `@` cannot conflict with a toplevel name *or* a name in a lower scope.  So the compiler will raise an error for something like this:

```
w> @ { 'a 1 'b 2 } { @ { 'a 1 'b 2 } a a b b }
Error. Cannot reassign `a`.
```

One last bit of deliciously decadent syntactic sugar. `@` can come *after* a named definition, in which case it will persist to *any* time the named definition is used and all of its subobjects.

```
w> b = 2 @ { 'a 1 }
w> c = + b a
3
w> b = { 6 7 } @ { a' 5 }
w> b (+ a 1)
7
```

In editors like VS Code, you can always see the currently defined names in the Wall inspector and their scopes.
 
## `set`

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
