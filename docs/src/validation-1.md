# Validation I

Wall's killer feature is validation of input.  For safe code, meaning code that exists only within the walls of Wall, validation is done at compile time. For unsafe code, meaning code that does some form of IO, the same validators that you use for your safe code can easily be used for your unsafe code.  So, conceptually, there is little to no distinction between validating dynamic input (ie the result of an API call) and making sure a function has valid input.

## Cumulative validation

The Wall compiler keeps a running tab of the strictest possible validation rule applicable to each value, named or unnamed.

```
w> c = 5
w> d = c + 1
w> { 6 7 } d
7
w> { 6 7 } c
Error. The function `{ 6 7 }` does not contain `5` in its domain.
```

It is important to note that the error above is a *compile-time* error, meaning that as you are typing the code in your editor or compiling it, Wall will complain.

```
w> a = floor (* 5 rand)
w> { 0 1 1 2 2 5 3 100 4 52 } a
100
w> a = floor (* 5 rand)
w> { 0 1 1 2 2 5 3 100 } a
Error. The function [ \ 0 1 \ 1 2 \ 2 5 \ 3 100 ] may not contain `a` in its domain.
w> { 0 1 1 2 2 5 3 100 } (// a 2)
1
```

Again, the error above is *compile-time* in Wall.

## Validators

Validators are functions that have every possible Wall value in their domain mapped to `true` or `false` in their range.

Wall comes with lots of validators already defined, like `int?`, `complex?`, `0?` etc.

```
w> int? 1
true
w> #chuck norris# =
w> #chuck norris?# #chuck norris#
true
w> 0? 1
false
```

The predefined function `:` will force a compilation error if a value does not pass the validator. This can be a useful form of documentation when working in teams or if you, like most people, are forgetful.

```
w> foo = : int? 5
w> foo
5
w> bar = : string? 5
Error. The key 5 does not exist on the object `:` string?.
```
 
 ## Writing validators

 Writing our own validators is easy!

 ```
 w> <5? = fmap! everything (? (int? k) (< k 5) false)
 w> <5? 0
 true
 w> <5? 5
 false
 w> <5? 'foo
 false
 ```