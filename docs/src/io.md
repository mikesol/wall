# IO

Wall's *raison d'etre* is IO.  While its compact syntax, dependent typing and  functional goodness are reason enough to use it, IO is where Wall shines.  While the IO can be reading to or writing from a file, making a network call or interacting with `stdin` and `stdout`, the basic idea is the same.  IO operations return a monad, and functions with validators or rules can act on that monad to produce other monads that are consumed by other parts of the program.

This means that IO can never cause a runtime error in Wall.  IO operations can of course report errors in their monads, but these errors flow through a Wall program thanks to Wall's system of monads and rules.

## `stdin`, `stdout` and `stderr`

To create a loop that reads `stdin`, you can do this:

```
// reader.wall
w> a = ? stdin 'read .== 'exit 0 a
a
```

```
$ wall reader.wall
hello
world
exit
$
```

You can write to `stdout` like this:

```
// writer.wall
stdout 'write 'foo
0
```

```
$ wall writer.wall
'foo
0
$
```

## Files

Files work very much like IO.

```
w> a = file 'r 'foo.txt
w> a
{ 'value 'hello }
w> b = file 'r 'does-not-exist
w> b
{ 'error "Thie file 'does-not-exist' does not exist" }
w> file 'w 'hello.txt 'world
{ 'written 'world }
w> file 'r 'hello.txt
{ 'value 'world }
w> a = file 'r 'foo.txt 'value
Error. The function `file 'r 'foo.txt` may not contain `value in its domain. 
```

## Network calls

We recommend using a high-level networking library for network `io`, like `wall-server` or `wall-client`.

```
w> \import ['http:get] 'wall-client
w> http:get 'https://www.randomstring.com
{ 'value 'foo }
```