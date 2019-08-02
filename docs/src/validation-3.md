# Validation III

Up until now, we have only seen validators that can accept or reject an argument.  In real life, this is rarely how things work.  We may want to accept an object if it meets certain criteria, reject it if it meets others, and modify it if it meets yet others.  In this section, we will look at *rules*. Rules, in Wall, produce a function that is in the form `{ 'success "what success looks like" }` *or* `false`.

## `rules`

Building rules in Wall is done with the `rules` function. `rules` accepts a list where each element is *either*

- a validator; *or*
- a two-element list with a validator and a function to be applied to the input if the validation succeeds; *or*
- a two-element list with a validator and a function to be applied to the input if the validation succeeds and a function to be applied to the input if the validation fails.

The rules in the list are applied from left to right.  As a convention, rules in Wall start with the letter `x`.

```
w> xAge = rules [int? [(>=? 0) id (just 0)] [(<? 150) id (just 150)]]
w> xAge 1
{ 'success 1 }
w> xAge -1
{ 'success 0 }
w> xAge 'foo
false
```

## Functions with rules

`fun` and `fun!` accept rules as well as validators.

```
w> xAge = rules [int? [(<? 0) (just 0)] [(>? 150) (just 150)]]
w> congrats = fun [xAge] `Congratulations! You are ${a0} years old!`
w> congrats 5
"Congratulations! You are 5 years old."
w> congrats -10
"Congratulations! You are 0 years old."
w> congrats 'bob
Error. The function `congrats` does not contain `'bob` in its domain.
```