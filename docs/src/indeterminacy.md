# Indeterminacy

There are some pre-defined Wall functions, like `rand`, `now` and `ptr`, that return different values every time a script is invoked and perhaps every time the element is encountered.  Let's check them out!

## `rand` and `rand0`

`rand` returns a random value with integer seed `n`.  `rand0` returns a random value with a seed of 0.  Because Wall does not contain 0-value functions, both `rand` and `rand0` require a value (any value) to be triggered.

```
w> a = rand0
w> b = a
w> == a b
true
w> == (a 0) (b 0)
false
```

## `now`

Now is the current timestamp, expressed as a float in microseconds since the beginning of the epoch.

```
w> a = now
w> b = a
w> == a b
false
w> a = now 0
w> b = a
w> a .== b
true
```

## `ptr`

`ptr` returns an string representing a `ptr` to an object in memory.

```
w> a = 1
w> ptr a
"0x510f32b"
```