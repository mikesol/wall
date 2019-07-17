# [Recursion II](/recursion-2)

A lot of pre-defined functions in Wall are defined using recursion.  For example, we have been creating lists in a rather annoying way so far by using the `\` function successively.  Wouldn't it be nice if we could create a list with a syntax like, for example, `foo 1 2 3 4 bar` to yield a list with `4 3 2 1`?  Recursion to the rescue!

```
w> bar () =
w> foo = map everything (flip \ (s+ foo [ \ bar (\ %k (%% bar))])) .s+ [ \ bar ()]
```

Yup, that is write-only code.  You may win at golf, but you would lose your job unelss you put a big fat comment.  That being said, let's unpack what's going on!

First, we are mapping everything to something and then taking its union with the set `[\ bar ()]`.  One way to think of `bar` is an aggregator: it holds the current value of whatever we want.  So, not surprisingly:

```
w> bar () =
w> foo = map everything (flip \ (s+ foo [ \ bar (\ %k (%% bar))])) .s+ [ \ bar ()]
w> foo bar
()
```

Then, in the middle part, we apply `\.flip (s+ foo [ \ bar (\ %k ((%% bar))) ])`.  The first thing to note is that we are flipping the application of `\`, so the last argument applied (which is what is being mapped from `everything`) will be the first element of our pair.  So, we are going to get some mapping of pairs where the first element corresponds to an element of everything.  Thus, according to Wall, it is a function.

Next, for the second part of the pair, we take a union between a function (`\.` - yay recursion!) and a set `[ \ bar (\ %k (%% bar)) ]`. From the Sugar chapter, we remember that `%k -1` is the key pointing to this function and `%% bar` is the value of `bar` up one level in the function.  In other words, we make a pair of the key pointing to this function and whatever the last value of `bar` was. So...

```
w> bar () =
w> foo = map everything (flip \ (s+ foo [ \ bar (\ %k (%% bar))])) .s+ [ \ bar ()]
w> foo 1 bar
\() 1 ()\
w> foo 1 2 bar
\() 2 1 ()\
w> foo 1 2 3 bar
\() 3 2 1 ()\
```

There are actually much shorter ways to accomplish this in Wall - the current code is verbose because we are only using what we have learned so far.  But even with this, we can create some pretty nifty functions.