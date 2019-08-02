# Example

We can combine functions and modules into powerful constructs to validate input at compile time.  Let's explore a short Wall program that shows some of these benefits.

In our program, we are calling an API called `randomstring.com` that returns a random string.

```
// random-string.wall
\import ['http:get] 'wall-client
body = (http:get 'https://www.randomstring.com) 'body
++ "Here's a random string:" ((parseJson body) 'result)
```

When we invoke wall with the `-e` flag for execute, we get the following error.

```
$ wall -e random-string.wall
Error. The function `parseJson body` may not contain the key `'result` in its domain.
```

We rewrite our program with the following tweaks.

```
// random-string.wall
\import ['http:get 'xJsonString] 'http-client
body = (http:get 'https://www.randomstring.com) 'body
input = xJsonString body
badNews = "Sorry, no random string today!"
goodNews = fmap! string (++ "Here's a random string:" k)
input == false ? badNews (goodNews (input 'success))
```

And now, when we run it...

```
$ wall -e random-string.wall
Here's a random string: foo.
$ wall -e random-string.wall
Here's a random string: bar.
$ wall -e random-string.wall
Sorry, no random string today.
```

In the function above, `xJsonString` is a rule provided in the `http` library, which is imported into `http-client`. Let's look at its definition:

```
// http.wall
xJsonString = rules [http:200? [http:json-response? parseJson] string?]
```

`xJsonString` will return `{ 'success "some string" }` upon success and `false` upon failure.