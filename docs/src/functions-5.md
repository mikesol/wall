# Functions V

We've already seen several different ways to define functions in Wall, but none of them resonate with the common pattern of `(arg1, arg2) => { /* do stuff */}` that we're used to in other languages.  Wall has a way to do this as well: `<<` and `<<!`.

## `<<` and `<<!`

`<<` is a predefined object that, intuitively, describes something that resembles a function in other languages.  Because `<<` is an aggregator (like our linked list function defined in [Recursion II](/recursion-2)), it needs a terminating character, which in this case is `>>`. The return value of `<< ... >>` is itself a map that iterates over a cross product of the argument space with no last argument.  The last argument, then, serves as the body of the function.

```
w> foo = <<! _? int? >> ? $> a1 5 0 a0
w> foo {} 6
{}
w> foo {} 5
0
```

`foo` is a function that takes two arguments, where the first can be anything and the second must be an integer. It returns `0` if the second argument is greater than `5`, else it returns the first argument.

`foo` produces arguments named `a0`, `a1` etc depending on the length of the input by using `@` under the hood.

Sometimes, it is useful to work with named arguments.  There is a version of `<<!` called `<<` that does that too.

```
w> foo = <<'a0 _? 'a1 int? >> ? $> a1 5 0 a0
w> foo {} 6
{}
w> foo {} 5
0
```

For the supremely lazy, there is `<<n` that takes `n` arguments that can be anything, or `_?`.

```
w> foo = <<n 3 map! $? (set? a0) a0 [a0] [ \ k (== a1 a2) ]
w> foo [1 2 3] 'foo 3.1416
[ \ 1 false \ 2 false \ 3 false ]
w> foo true 'foo 3.1416
[ \ true false ]
```
