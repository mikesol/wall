# Tests II

Tests in Wall are not tests in the conventional sense, where a test runner runs a battery of tests and they succeed or fail. While this is possible, it requires an additional level of orchestration. Tests that are co-located in files do not work this way. Instead, these tests run at *compile time*.

## `expect`

Like many test runners, Wall has an assertion-like syntax based on the word `expect`. Here is a simple test in Wall:

```
// simple-test.wall
@begin-test
expect (1.+ 1) 'toBe 2
@end-test
```

Let's look at a simplified definition of the function `expect`.

```
w> expect = fmap!a everything {
  'toBe (fmap!b everything ({ true "Works" } (== a b)))
}
```

Because of Wall's [property-based validation](./validation-1), if `(== a b)` has the property of anything other than "is true", the compilation will fail. In this way, one can think of all tests in Wall as property-based tests.

Sometimes, it is useful to create a value that represents the entire range of possible values for a given property.  For example, while the value `0.5` corresponds to the property "between 0.0 inclusive and 1.0 exclusive", there are other values that have this property as well. `rand 0`, on the other hand, could theoretically generate every number that has the quality "between 0.0 inclusive and 1.0 exclusive."

```
w> expect (rand 0) 'toBeGreaterThanOrEqualTo 0.0
"Input is greater than or equal to output."
w> expect (rand 0) 'toBeGreaterThan 0.0
Compilation error. The function `expect (rand 0) 'toBeGreaterThan` may not contain the value `0.0` in its domain.
```

While in this case it is easy to generate a value having the quality we want, how can we generate a value having a more complex property, like a function that has `1` in its domain?

To do this, we can use the function `choose`. Even though we have no way to verify what that value is, we can use it to do property-based testing.

```
// augment-counter.wall
@begin-test "`increment-counter` increases a counter by 1"
x = choose (dom increment-counter)
expect (increment-counter x 'counter) 'toBe (+ (x 'counter) 1)
@end-test

has-counter? = def [_?] (
    a0.function? .& (a0.has? 'counter) .& (a0 'counter).int?)
increment-counter = def [has-counter?] (+ 'counter.a0 1)
```

