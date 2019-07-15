# Functions V

We've already seen several different ways to define functions in Wall, but none of them resonate with the common pattern of `(arg1, arg2) => { /* do stuff */}` that we're used to in other languages.  Wall has a way to do this as well: `def` and `def!`.

## `def` and `def!`

`def` is a predefined object that, intuitively, describes something that resembles a function in other languages.  Because `def` is an aggregator (like our linked list function defined in [Recursion II](/recursion-2)), it needs 

```
w> foo$ = def _? int? fed @ { a0 %%k a1 %k } (> a1 5).? 0 a0
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