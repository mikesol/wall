# Validation III

Up until now, we have only seen validators that can accept or reject an argument.  In real life, this is rarely how things work.  We may want to accept an object if it meets certain criteria, reject it if it meets others, and modify it if it meets yet others.  In this section, we will look at *rules*. Rules, in Wall, produce a pair that is in the form `\ 'success _?` *or* `false`.

## `rules`

Building rules in Wall is done with the `rules` aggregator function. `rules` accepts *either* validators *or* a pair with a validator and a change to be performed if the validator fails.  `rules` will apply itself until the validator passes or fails, and if it can potentially result in infinite recursion, it will raise a compilation error.

```
w> age-rule = rules int? \ (<? 0) (just 0) \ (>? 150) (just 150) ;
w> age-rule 1
\ 'success 1
w> age-rule -1
\ 'success 0
w> age-rule 'foo
false
```

## Functions with rules

The family of `<< >>` function creators accept rules as well as validators.

```
w> congrats! = <<! age-rule >> `Congratulations! You are ${} years old!`
w> congrats! 5
"Congratulations! You are 5 years old."
w> congrats! -10
"Congratulations! You are 0 years old."
w> congrats! 'bob
Error. The function `congrats!` does not contain 'bob in its domain.
```