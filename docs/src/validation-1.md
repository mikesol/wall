# Validation I

Wall's killer feature is validation of input.  For safe code, meaning code that exists only within the walls of Wall, validation is done at compile time. For unsafe code, meaning code that does some form of IO, the same validators that you use for your safe code can easily be used for your unsafe code.  So, conceptually, there is little to no distinction between validating dynamic input (ie the result of an API call) and making sure a function has valid input.

## Cumulative validation

The Wall compiler keeps a running tab of the strictest possible validation rule applicable to each value, named or unnamed.

```
w> c = 5
w> d = c + 1
w> [ \ 6 7 ] d
7
w> [ \ 6 7 ] c
Error. The function [ \ 6 7 ] does not contain 5 in its domain.
```

It is important to note that the error above is a *compile-time* error, meaning that as you are typing the code in your editor or compiling it, Wall will complain.

```
w> a = floor (* 5 rand)
w> [ \ 0 1 \ 1 2 \ 2 5 \ 3 100 \ 4 52 ] a
100
w> a = floor (* 5 rand)
w> [ \ 0 1 \ 1 2 \ 2 5 \ 3 100 ] a
Error. The domain of the function [ \ 0 1 \ 1 2 \ 2 5 \ 3 100 ] is not a superset of possible values for a:[0 1 2 3 4].
w> [ \ 0 1 \ 1 2 \ 2 5 \ 3 100 ] (// a 2)
1
```

Again, the error above is *compile-time* in Wall.

## Our first validators

Validators are functions that have every possible Wall value in their domain mapped to `true` or `false` in their range.

Our first validator, which we will call `exists?`, will return `true` if something exists and `false` if it doesn't.  As everything in Wall exists, it will always return `true`.

```
w> exists? = map everything (flip \ true)
w> exists? 1
true
w> exists? 2
false
```

Building upon the success of our first validator, our second validor `does-not-exist?` will check if a thing does not exist.  Of course, as the thing needs to exist to inquire about its existance, this validator will always return `false`.

```
w> does-not-exist? = map everything (flip \ false)
w> does-not-exist? 1
false
w> does-not-exist? 2
false
```

Wall comes with lots of validators already defined, like `int?`, `complex?`, `0?` etc.

```
w> int? 1
true
w> #chuck norris# =
w> #chuck norris?# #chuck norris#
true
w> 0? 1
false
w> == int? (s+ (map (s- everything int) (flip \ false)) (map int (flip \ true)))
true
```

The predefined function `:` will force a compilation error if a value does not pass the validator. This can be a useful form of documentation when working in teams or if you, like most people, are forgetful.

```
w> foo = : int? 5
w> foo
5
w> bar = : string? 5
Error. The key 5 does not exist on the object `:` string?.
```
 