# IO

All wall IO operations return two streams - one for input and one for output - and a success code. The form of this is `{ 'i: <stream>, 'o: <stream> 'code: <0 -1 -2 ...> }` While the code varies according to the operation, `0` always represents success. In case of failure, the length and content of the stream is undefined.

## Streams

The function `read` takes a readable stream and a number of bytes to read as its arguments and returns a function in the form `{ 'bytes: <byte string>, 'read: <int> }`.

The function `write` takes a writeable stream and a byte string as its arguments and returns the number of bytes written as an integer.

## Files

File IO operations are created by specifying 'r or 'w and then the name of the file.

```
w> a = file 'r 'foo.txt
w> a
{ 'i: <./foo.txt>, 'o: <./dev/null>, 'code: 0 }
w> b = file 'r 'does-not-exist
w> b
{ 'i: <./does-not-exist>, 'o: <./dev/null>, 'code: -1 }
w> write (file 'w 'hello.txt 'o) b"world"
5
w> read (file 'r 'hello.txt 'i) 5
b"world"
```

In addition to files persisted to disk, `file` supports standard posix pipes like `/dev/stdin`.