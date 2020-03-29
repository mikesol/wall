# Indeterminacy

There are some pre-defined Wall functions, like `rand`, `now` and `ptr`, that return different values every time a script is invoked and perhaps every time the element is encountered.  Let's check them out!

## `rand`

`rand` returns a random value generator seeded with integer seed `n`. The result of `rand n` is triggered by passing it any value.

```
w> rand-seeded-with-5 = rand 5
w> rand-seeded-with-5 'hello
0.3425601241
w> rand-seeded-with-5 'hello
0.0943142369
```

## `now`

Now is the current timestamp, expressed as a float in microseconds since the beginning of the epoch. Now needs to be invoked with any key as input.

```
w> now _
1585472068494
```

## `ptr`

`ptr` returns an string representing a `ptr` to an object in memory.

```
w> a = 1
w> ptr a
"0x510f32b"
```