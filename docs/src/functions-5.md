# Wall

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
\import ['http:get] 'http-client
\import ['isJsonString?] 'json
body = (http:get 'https://www.randomstring.com) 'body
input = rules [[isJsonString?] (parseJson body)]
++ "Here's a random string:" ((parseJson body) 'result)
```