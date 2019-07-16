# Threading

Wall, like Node.js, has an opinionated view on threading that is not possible to change without fiddling with compiler options or messing around with internals.  That said, we think it provides a sensible default for all but the most esoteric cases.

Because order of execution in Wall is not guaranteed, Wall will aggressively optimize to frontload as many operations as possible on as many threads as authorized by the threading limit.  Under the hood, it rewrites algorithms to most efficiently process on a given architecture, creating different versions depending on the input data for functions that can have different outcomes because of an IO call or other side effect.

However, sometimes, you want to create a before-after relationship between two objects.  The function `b-a` does that.

## `b-a`

`b-a val0 val1` is a contract between two named values that expresses the following relationship:

- all operations that `val0` must completely execute before `val1` begins
- if when `val0` there is no longer a viable code path to `val1`, `val1` will not be computed.

`b-a` returns a pair of the two values.

```
// eager.wall
a = file 'w 'foo.txt 'hello
b = file 'w 'bar.txt 'world
? a.has-not? 'error (a 'value) $? b.has-not? 'error (b 'value) (b 'value) "Write error!"
```

```
// lazy.wall
{ a car b cdr } = b-a (file 'w 'foo.txt 'hello) (file 'w 'bar.txt 'world)
? a.has-not? 'error (a 'value) $? b.has-not? 'error (b 'value) (b 'value) "Write error!"
```

```
$ wall eager.wall
$ ls
eager.wall lazy.wall foo.txt bar.txt
$ rm foo.txt bar.txt
$ wall lazy.wall
$ ls
eager.wall lazy.wall foo.txt
```