# [Recursion](/recursion)

In Wall, any function can refer to itself in its definition.  Here is the famous [McCarthy 91](https://en.wikipedia.org/wiki/McCarthy_91_function) function written in Wall.

```
w> mc = fun [int?] $? (100.< a0) (a0.- 10) (mc (mc (a0.+ 11)))
w> mc -100
91
w> mc 5
91
w> mc 90
91
w> mc 1000
990
```
