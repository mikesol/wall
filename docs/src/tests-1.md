# Tests I

In Wall, tests can be colocated with code or in their own files.  They exist in blocks that start with `@begin-test` and end with `@end-test`.  The named values in these blocks are unavailable to the rest of the file.

Variables that should be used by all tests can be defined in `@begin-before-all`, which will execute before all tests, or `@begin-before-each`, which will execute before each test.

```
// my-code.wall

@begin-before-all
foo = 'foo
baz = 'baz
@end-before-all

@begin-test "'foo is defined the same as 'baz in my-func"
a = my-func foo
b = my-func baz
expectEquals a b
@end-test

my-func = { 'foo: 'bar, 'baz: 'bar }
```

```
$ wall -test my-code.wall
pass "'foo is defined the same as 'baz"
```