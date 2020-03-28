# Guards I

We have seen that Wall validates input whenever there is a function invocation. When it sees `f a`, it asks itself, "Given the properties I know about `f` and `a`, does there exist a possible value of `a` that is not in the domain of `f`?" There are many ways to construct a domain for a function `f`, but one common way is by using **guards**. In this section, we will introduce guards, and in subsequent sections, we will see how they can be used to define functions.

## Hello guards

Guards are functions that have every possible Wall value in their domain mapped to `true` or `false` in their range.

Wall comes with lots of guards already defined, like `int?`, `complex?`, `0?` etc.

```
w> int? 1
true
w> #chuck norris# =
w> #chuck norris?# #chuck norris#
true
w> 0? 1
false
```

The predefined function `:` will force a compilation error if a value does not pass the guard. This can be a useful form of documentation when working in teams or if you, like most people, are forgetful.

```
w> foo = : int? 5
w> foo
5
w> bar = : string? 5
Error. The key 5 does not exist on the object `:` string?.
```
 
 ## Writing guards

 Writing our own guards is easy!

 ```
 w> <5? = fmap! everything (? (int? k) (< k 5) false)
 w> <5? 0
 true
 w> <5? 5
 false
 w> <5? 'foo
 false
 ```