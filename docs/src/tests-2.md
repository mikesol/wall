# Tests II

In most languages, a testing framework (ie [ava](https://github.com/avajs/ava) in JavaScript, [pytest](https://docs.pytest.org/en/latest/) in Python) is used to exeute a group of tests.

In Wall, tests that are co-located in files do not work this way. Instead, these tests execute at *compile time*.

## `expectEquals`

Here is a simple test in Wall:

```
// simple-test.wall
@begin-test
expectEquals (+ 1 1) 2
@end-test
```

Let's look at the definition of the function `expectEquals`.

```
w> expectEquals = fun [_ _] ({ true } (== %k %%k))
```

As an exercise, try to spot how this function forces a compile error if `%k` `%%k` are not equal. Remember that `{ true }` is the function `{ true: true }` and that it invokes a bound version of `(== %k %%k)`.