 
# Predefined things

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
 
## `float`

Wall comes with a few predefined `float`-s that are sometimes useful.

```
w> rand
0.055325461
w> now
1562524244.200712
```

Because Wall evaluates lazily, these `float`-s will evaluate only when they need to. To force evaluation, you can use the `!` variants of both.

```
w> rand!
0.055325461
w> now!
1562524244.200712
```
 
## `object`

Wall has lots of predefined `object`-s.  In this section, we'll cover several of the most popular predefined objects.  A full reference of predefined objects can be found [here](/reference). In the [Examples](/examples) section, we will create our own versions of some predefined objects.
 
### `choose`

Choose can be thought of as the following: a magical `object` that contains every conceivable `set` and `object` in its keys, and its values are always an element of the key when the key is a `set` or a key within the key when the key is an `object`. Sounds heavy, but it's not. Let's see it in action:

```
w> choose [1 2 3]
1
w> choose [1 2 3]
2
w> choose [1 2 3]
1
w> choose { 1 2 3 4 5 6 }
5
w> choose { 1 2 3 4 5 6 }
3
w> choose { 1 2 3 4 5 6 }
3
```

Importantly, `choose []` is `$` and `choose {}` is `$`.

```
w> choose []
$
w> choose {}
$
w> choose [$]
$
w> choose { $ 1 }
$
w> choose { 1 $ }
$
```
 
### `suc`

`suc` is the successor function. It is defined on members of `int` and `float`.

```
w> suc 1
2
w> suc -999.999
w> -998.999
```

### `pre`

`pre` is the predecessor function. It is defined on members of `int` and `float`.

```
w> pre 1
0
w> pre -999.999
w> -1000.999
```

### `'`, `"`, and ``` ` ```

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
w> str? "abc"
true
w> s.ss "abc" 0
"a"
w> s.ss "peace" rg 0 5
"pe"
w> s.ss "שלום" O
"ש"
w> s.s "שלום peace" 0
"ש"
w> s.s "שלום peace" rg 0 5
"שלום p"
w> s.s "שלום peace" 5
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

### `d-1`, `d-2` and `d-n`

Arbitrary delayed application of `object` keys can be created with the family of `d-` `object`-s.

```
w> a = d-1 (+ [0]) key
w> a { 3 4 }
[0 3]
w> b = d-2 (+ [0]) map
w> b [0 1] (+ 1)
[0 1 2]
w> c = d-2 (* 7) +
w> c 3 2
42
```

Here, we are saying "take the last key, apply `-n` keys to it, and then use it as a key in the preceding key.

### `not`, `&`, `|`, `x|`, `xn|`, `if` and `iff`

The operators `not`, `&`, `|`, `x|`, `xn|`, `if` and `iff` all work on `bool`, and some of them pull triple duty for `bool`, `set` and `object`.

```
w> & true false
false
w> & [0] [1]
[0 1]
w> x| false false
true
```

The `object` union operator also has a recursive variant that merges objects with similar keys when possible instead of replacing the content.

```
w> &! { 0 { 1 2 }} { 0 { 3 4 }}
{0 { 1 2 3 4 }}
```

### `==` and `/=`

Wall defines equality as "being the same or containing the same things."

```
w> == 1 1
true
w> == 1 (+ 0 1)
true
w> == [1 2 3] [1 2 (+ 1 2)]
true
w> == [1 2 3] [3 2 1 $]
true
w> == { 0 { 0 1 } } { 0 { 0 1 } }
true
w> == (m-2 not >=) <
true
w> == (m-2 not >) <
false
w> == (&! (m-2 not >) (red (map! int { k { k false } }) &)) <
true
```

### `def`

`def` is a predefined object that, intuitively, describes something that resembles a function in other languages. As a convention, all function names should end with `$`.

```
w> foo$ = def _? int? fed @ { a0 ...k a1 .k } (? (> a1 5) 0 a0)
w> foo$ {} 6
{}
w> foo$ {} 5
{}
```

In other languages, we would say something like:

> `foo$` is a function that takes two arguments, where the first can be anything and the second must be an integer. It returns `0` if the second argument is greater than `5`, else it returns the first argument.

In Wall, we'd say:

> `foo$` is a nested object. `k` can be anything. `v.k` must be an integer. And `v.v` is `0` or `k` depending if `v.k` is greater than `5`.

Sometimes, it is useful to work with named arguments.  There is a version of `def` called `def!` that does that too by applying `@` internally.

```
w> foo$ = def! 'a0 _? 'a1 int? fed (? (> a1 5) 0 a0)
w> foo$ {} 6
{}
w> foo$ {} 5
{}
```
 
### `rev`

`def` allows for lots of goodies that people coming from the functional programming world love. Currying of arguments. Currying of signatures.  Accessing curried arguments. With respect to the latter, we have `rev+` and `rev-`.

```
w> < 5 4
false
w> rev+ < 5 4
true 
```

`rev-` reverses the previous key with the incoming key of a binary function. Remember: we can do this because the previous key is always accessible via the `.k` operator.

```
w> < 5 4
false
w> rev- (< 5) 4
true
```
 
### `red`

Sometimes, you want to reduce the key/value pairs in an `object` or `set`, like summing them up. That's done with `red`.

```
w> red [1 2 3] + 0
6
w> red [{'a 1} {'b 2} {'c 3}] & {}
{'a 1 'b 2 'c 3}
w> red! { 0 5 1 4 2 3 } (rev & {k (? (< k 1) (+ k v) $)}) {}
{ 2 5 }
w> red! [8 3 2] (& a (? (< k 4) (+ k 3) 0)) []
[11 0 0]
```

`red` is an `object` that is three levels deep.  Here are the keys that can be fed to it:

- Level 1: A `set` or an `object`.
- Level 2: A three-level `object` for `set`-s, and a four-level `object` for `object`-s. The first level is the aggregated `thing` that came from the last application of this `object`. The second level is an element from the `set` or a key from an `object`. For `object`-s, the third level is the value from the `object`. The last level should represent the result of the aggregation.
- Level 3: An initial `set` or `object` applied as a key to level 2.

In its variant `red!`, some `thing`-s from level two are injected via `@` into the current context.

- `a` is the aggregator
- `k` is the element or key
- `v` is the value in the case of `object`-s.
 
### `map`

In the above example, the last two `red` show a similar pattern - taking the successive union of an object. This happens so often that there is a bit of syntactic sugar in Wall, `map`, to facilitate that.  Below are the two examples from `red` rewritten in `map`.

```
w> map! { 0 5 1 4 2 3 } {k (? (< k 1) (+ k v) $)}
{ 2 5 }
w> map [8 3 2] (? (< k 4) (+ k 3) 0)
[11 0 0]
```

## `set`

As mentioned, there are five predefined sets: `int`, `float`, `bool`, `symbol`, and `object`.  Thankfully, these `set`-s ship with the wall compiler.  Defining them manually would take a long, long time.

There are two ways to check if a `thing` belongs to a `set`.

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

## ordered things

There is no predefined way to create ordered things in Wall. You can, however, create an object that functions like an array in languages like JavaScript.

```
w> a = { 0 5 1 2 2 6 }
w> a 0
5
w> a 1
2
```

It is also possible to create linked lists.

```
w> ll = def! 'a _? b fed { 'k a 'v ll }
w> z = ll 1 'v 2 'v 3 'v 4 $
w> z 'k
1
w> z 'v 'k
2
```