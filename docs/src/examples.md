# Examples

## Alternative predefined objects

Let's make two alternatives to `+` and call them `+'` and `+''`.

```
w> +' = def! 'a int? 'b int? fed
  (? (& (> a 0) (> b 0))
    (+' (pre a) (suc b))
    (? (& (< a 0) (< b 0)))
      (neg (+' (neg a) (neg b)))
      (? (== a 0)
        b
        (? (== b 0)
          a
          (? (< a 0)
            (- b (neg a)) (- a (neg b)))))))
w> +'' = rev +' 
w> == + +'
true
w> == +' +''
w> == (+ 3) (+'' 3)
true
```

Remember that, in Wall, equality of objects traverses the objects and makes sure that the keys of the two objects are the same set and that these keys point to the same values. `+`, `+'` and `+''` all have the same key-value pairs, so they hold under `==`.

## Fun with sets

You can construct arbitrary set in Wall and explore their properties.

```
w> a = map! int { a (? (>= a 0) a $) }
w> b = (- int a)
w> (== (key +) (+ float (+ a b)))
true
w> (== (key /) (+ float int))
false
w> (== (key /) (- (+ float int) [0 0.0]))
true
```