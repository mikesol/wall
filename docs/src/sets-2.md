# Sets II

Wall has several predefined sets.  Some of them resemble types in other languages, like `int`, `string`, `symbol` and `complex`. In Wall, `int` is the set of all integers, `string` is the set of all strings, `symbol` is the set of all symbols and `complex` is the set of all complex numbers.

```
w> int .== (s+e int 0)
true
w> string .== (s+e string 0)
false
w> foo =
w> symbol foo
true
w> subs? int complex
true
```

## `everything`

There is one special set called `everything` that contains everything that Wall does or will ever contain, including itself.

```
w> int.subs? everything
true
w> everything.s- everything
:[]
w> everything.subs? everything
true
```

## Sets are like guards

If you're coming from a language like Erlang or Clojure, you may be familiar with **guards**.  In these language, a guard accepts any value and returns `true` or `false` depending on what the value is.  In Wall, guards are just sets.

Guards are no different than [sets](./sets-1): they are functions that contain every possible Wall value in their domain mapped to `true` or `false` in their range. Below, let's define a set (or guard) that checks if an integer is greater than 5.

```
w> gt5? = (filt-s int (> 5))
w> gt5? 6
true
w> gt5? 5
false
w> gt5? 'foo
false
```