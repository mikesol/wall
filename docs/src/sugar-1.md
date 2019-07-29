# Sugar I

Like lots of other languages, Wall has some delicious morcels of syntactic sugar that make it a little easier to read and write code.  We have already seen one piece of sugar, `=`, that allows you to name things.  Let's check out some more!


## Parentheses

By default, all function invocations in Wall are maximally *greedy*.  That is, when invoked, they will try to gobble anything to the left of them, even if it is a function.

```
w> name = { > "greater than" < "less than" }
w> name <
"less than"
```

However, sometimes, we don't want this at all.  Consider the following case:

```
w> == == 3 4 == 4 5
Error. `false` is not a function.
```

Intuitively, we would like to ask "Is 3 == 4 equal to 4 == 5?".  We can do this with parentheses.  Let's revisit the `==` example above, but use parentheses to make it work.

```
w> == (== 3 4) (== 4 5)
true
```

Here, the parentheses say to Wall "hey, forget about that greedy `==` for a second. Let's figure out what's inside here first, and then we'll feed it to the `==`."

One important thing to note is that sets, lists and functions suspend **all** function invocation within their definitions.  That means that `[& true false]` is a list that has three members: `&`, `true`, and `false`.  To evaluate the function, it has to be enclosed in parentheses.

```
w> [& true false]
[& true false]
w> [(& true false)]
[false]
```

## Dots

The `.` symbol in Wall *flips* function invocation so that what comes *after* the period calls whatever comes before the period.  Whitespace is optional both before and after the dot.

```
w> (3 .== 4) .== (4 .== 5)
```

The dot syntax allows anything in Wall to become an infix operator, which makes it look and feel a bit more like Python or JavaScript.

## Dollars

It is fitting that, when talking about a greedy protocol, we conclude with a discussion of the `$` sign.  `$` in Wall means "suspend the current stack and open a new one until there is no function on the new stack anymore *or* until there is a newline".

```
w> ? false 0 $? false 1 $? true 2 $? false 3 4
2
```

## Dotted dollars

Lastly, the `.$` sign combines `.` and `$` into one uber sign.

```
w> 6 .$- 5 .$- 4 .- 3
2
w> == (6 .$- 5 .$- 4 .- 3) (- 6 (- 5 (- 4 3)))
true
w> 6 .- 5 .- 4 .- 3
-6
w> == (6 .- 5 .- 4 .- 3) (- (- (- 6 5) 4) 3)
true
```

We have already seen two of them: `.` and `$`.  In editors, sugar is colored differently, and sugar can *never* be interpreted as symbols or named values.  That means that you can't do something like:

```
w> [ $ . ]
Error. Cannot understand how to use `$`.
Error. Cannot understand how to use `.`.
```

## Percent

Sometimes, when working with functions, it is useful to refer to elements higher up in the function's heirarchy.  One way to do this is to manually create these references.

```
w> #one level back# =
w> c = { 'level 'c }
w> b = { 'level 'b 'next (f+ { #one level back# b } c) }
w> a = { 'level 'a 'next (f+ { #one level back# a } b) }
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
w> a = { 'a { %k (%% 'b) } 'b 1 }
w> b = { 'a { %k! (%%! 'b) } 'b 1 }
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
