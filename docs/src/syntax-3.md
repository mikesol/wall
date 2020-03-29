# Syntax III

Here are some more syntactical conventions in wall

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

## Pattern matching

Pattern matching works in assignment or in `@` blocks.  Patterns are always functions that map value names to operations on the object on the right that would yield that value.

```
w> { 'a id 'b id } = { 'a 0 'b 1 }
w> a
0
w> b
1
```

Note that pattern matching only works on parts of values that have no ambiguity.  If an object is created conditionally based on a random value or IO operation, pattern matching will only work on the part of the object that is non-random.

## The `!` family

We've seen functions like `map` and `red`, but they have much more usable variants called `map!` and `red!` that use `@` under the hood to create some yummy named things.

```
w> min0x = fmap! int (? (< k 0) 0 k)
w> min0x 4
4
w> min0x -1
0
```

The same is true of `red` - `red!` injects the accumulator `a` and the key `k`.

```
w> red! [1 2 3] (+ a (* 2 k)) 0
12
```

## Namespace conflicts

As mentioned, Wall does not allow for two elements to have the same name in the same scope *or* in nested scopes.  This poses a challenge if we want to nest maps.  To get around it, we have the following (very lazy) versions for *map* and *red* that create different variable names in the range of `a-z`.

```
w> foo = [[1 2] [3] [4 5 6]]
w> map!a foo (map!b a (+ b 1))
[ [ 2 3 ] [ 4 ] [ 5 6 7 ] ]
```