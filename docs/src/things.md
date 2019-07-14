 
# Things

In Wall, stuff like `5`, `true`, `[1 2 3]` or `{ 'foo 'bar }` are called `thing`-s. Every `thing` in Wall belongs to one or several predefined `set`-s.  If you're coming from Haskell or TypeScript or Fortran (or almost anything else), `set`-s are roughly equivalent to types.

Wall has lots of predefined `set`-s: `int`, `float`, `complex`, `bool`, `string`, `symbol`, and `object` are all examples of `set`-s.  `thing` is a `set` as well.

```
w> in? 1.0 float
true
w> in? 1 int
true
w> in? 1 float
false
w> in? 1+3j complex
true
w> in? [1] set
true
w> in? 1 thing
true
w> in? int thing
true
w> in? thing thing
false
```

Any `thing` can be given a name in Wall. Named things are immutable, meaning once they are created, they cannot be changed. Names in Wall cannot contain whitespace and cannot begin with a `.`. Otherwise, they can be anything that is not predefined by the language.

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

`float`-s are represented as double-precision floating numbers in Wall.

```
w> 5.1
5.1
w> 0.0
0.0
w> -1.3
-1.3
w> -1_000_000_000.000_000
1_000_000_000.0
w> -999999.001_300_0
-999_999.0013
```


## `complex`

`complex` numbers work like `int`-s and `float`-s: the real part can be either an `int` or a `float`, and the imaginary part can be an `int` or a `float`.  Note that, to define a complex number, you must either separate the real and imaginary part by `+` or `-` or use the `.` postfix notation.

```
w> 0-4j
0-4j
w> 1+3.2j
1+3.2j
w> 4j .+ 3.1416 
3.1416+4j
```


## `bool`

Like in other languages, a `bool` can be `true` or `false`.

```
w> a = true
w> b = false
w> a .is? b
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

You've already seen two predefined symbols - `true` and `false` - above.  In general, symbols should be used in application-specific domains.

## `string`

In Wall, `string`-s can be created three different ways:

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
w> str? "abc"
true
w> "abc" 0
"a"
w> "peace" 0~5
"pe"
w> "שלום" O
"ש"
w> "שלום peace" 0
"ש"
w> "שלום peace" 0~5
"שלום p"
w> "שלום peace" 5
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

## `object`

An object in Wall is just a collection of keys and values, where keys can be any `thing` and values can as well. While an object can have the same value for several different keys, the reverse is not true.

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

Values can also be retrieved in a postfix manner using the symbol `.`, which reverses the order of execution.

```
w> b = { 5 3 'c 4 }
w> 5.b
3
```

Sometimes, when constructing or destructuring an `object`, it's useful to refer to other bits of the `object`. You can do that with the following syntactic sugar:

- `%`: the present `object`.
- `%k`: the key that points to this `object` in the enclosing `object`.
- `%%`: the enclosing `object`
- `%%k`: the key that points to the enclosing `object`.

%%% and so forth and so on.

Sometimes, you want to refer to other bits of an `object`-s *original* enclosing `object`.  To do this, we use the same convention as above, but ending with an exclamation point:

- `%!`: the *original* present object.
- `%k!`: the *original* key that points to this `object` in the enclosing `object`.
- `%%!`: the *original* enclosing `object`
- `%%k!`: the *original* key that points to the enclosing `object`.

```
w> a = { 'a { %k %% %k } }
w> b = { 'a { %k! %%! %k! } }
w> a 'a
{ 'a ' a }
w> b 'a
{ 'a 'a }
w> c = { 'q a 'a }
w> d = { 'q b 'a }
w> c q'
{ 'q 'q }
w> d q'
{ 'a 'a }
```

Because the un-exclamationed form of `%k`, `%%` etc resolves to *any* enclosing object, there will be no compiler error until you attempt to *access* an object with `%k`, `%%` etc.

```
w> a = { %k %%k }
w> b = { %k! %%k! }
Error. %% b is not an object.
w> c = { 0 a }
w> d = { 0 { 1 a } }
w> d 0 1
{ 1 0 }
w> c 0
Error. %% c is not an object. 
```

## `set`

A set in Wall is a collection of **unordered** items.

```
w> [1 2 3]
[1 2 3]
w> 1.in? [1 2 3]
true
```

The special element `\` works similar as in an `object` - it is ignored.

```
w> [1 2 \]
[1 2]
w> [1 2] & [\]
[1 2]
w> len [1 \]
1
```

## Hints

Hints are used to communicate directly with Wall. They are syntactic sugar: every hint could have a longer variant, but life is short, so why wait?

## `@`

The most important hint in Wall is `@`. `@`, like `let` in Haskell, can be used to create ephemeral named `thing`-s in a computational context. `@` takes an object whose keys are valid names. There can be as many `@`-s as one likes before the object. 

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


### `$`

The `$` hint, like in Haskell, makes the suspends the greediness of the preceding object and makes the upcoming object greedy.  It can be prepended to any object, which means that named `thing`-s cannot start with `$`.  This is especially useful for sequential if/then statements.

```
w> foo = def! 'i int? fed ? (> 5 i) 1 $? (> 0 i) 2 3
w> foo 10
1
w> foo 2
2
w> foo -100
3
```

### `.`

As we've seen before, the postfix hint transforms anything object accessor into a postfix operation that has the same precedence as the prefix operation.  This can be chained with `$` to change the precedence as well

```
w> (+ (- 5 1) (* 6 7))
46
w> 5.- 1.+ (* 6 7)
46
w> 5.- 1.+ 6 .$* 7
46
```

### `!`

The bang hint, or `!`, tells Wall to evaluate something *now*. This is useful when, for example, you would like a value to evaluate immediately.

```
w> c = - now !now 
w> // wait 1 second
w> c
1000.0
```

### `\`


The `\` hint in objects means "ignore me" when used as a key or value.

```
w> a = { 'a \ }
w> a
{ }
w> is? { 'a \ 'b \ } {}
true
w> is? { \ 0 \ 3 } {}
true
```
