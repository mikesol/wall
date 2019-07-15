# Numbers

There are three primitive numeric types in Wall: `int`, `float` and `complex`.

## `int`

In Wall, `int` represents and integer (surprise!). Integers in Wall are unbounded, which means they can be as big or tiny as you'd like to be. Groups of three digits can be separated by an underscore (`_`).

```
w> 5
5
w> 0
0
w> -1
-1
w> -0
0
w> 1_000_000_000
1_000_000_000
w> -999999
-999_999
```

## `float`

`float`-s are represented as double-precision floating numbers in Wall.

```
w> 5.1
5.1
w> 0.0
0.0
w> -1.3
-1.3
w> -1_000_000_000.000_000
1_000_000_000.0
w> -999999.001_300_0
-999_999.0013
```


## `complex`

`complex` numbers work like `int`-s and `float`-s: the real part can be either an `int` or a `float`, and the imaginary part can be an `int` or a `float`.  Note that, to define a complex number, you must either separate the real and imaginary part by `+` or `-` or use the `.` postfix notation.

```
w> 0-4j
0-4j
w> 1+3.2j
1+3.2j
w> 4j .+ 3.1416 
3.1416+4j
```
