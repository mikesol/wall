# Tests I

In Wall, tests can be colocated with code or in their own files.  They exist in blocks that start with `@begin-test` and end with `@end-test`.  The named values in these blocks are unavailable to the rest of the file.

```
// american-emotional-lexicon.wall

@begin-test "Americans are only ever happy"
american-happiness = amerian-emotional-lexicon 'happy
american-sadness = american-emotional-lexicon 'sad
expectEquals american-happiness american-sadness
@end-test

american-emotional-lexicon = map _ 'happy
```

In Wall, all tests execute at **compile time** using functional domain verification.

```
$ wall american-emotional-lexicon.wall
pass "Americans are only ever happy"
```