# Functions VI

You've already seen Wall functions that return functions.  Furthermore, it is easy to create a Wall function that manipulates functions after they're defined.

```
w> notter = map!!a-b | \ (not a) (map!!c-d b \ (not c) (not d))
w> not| = notter |
w> not| true false
false
w> not| true true
true
```

A function can also be defined using a list.

```
w> f-com? = (complex .->? complex .->? complex) .|?? (complex .->? complex) .|?? complex?
w> narg = <<! f-com? >> ? a0.complex? (neg a0) (a0 narg)
w> nargify = <<! (f& list? (l-elts? (yfi f-com))) >> red!:() a0 invoke id
w> neg-f0 = <<! complex? complex? >> nargify list + * a0 a1 - a0 a1 ** a0 ;
w> neg-f1 = <<! complex? complex? >> nargify list / - a1 a0 * a0 a1 ;
w> neg-f0 3 4
3
w> neg-f1 3 4
-3
```

Remembering that `(` is a function, we can also define functions that process ordinary function definitions enclosed in parentheses so long as `(` and `)` are in the domain of the function.

This pattern helps us gives us the tools we need to effectively handle monads in Wall.

## Fortune telling

As an example, you could imagine that a function generates a fortune for a given horoscope.

```
w> /import [gen-fortune] from 'horoscope
w> gen-fortune 'Scorpio
"Bad stuff gonna go down."
w> gen-fortune 'Libra
"Check out Scorpio."
```

One day, the person that made `gen-fortune` desides to create another function `gen-fortune-2` that returns a bunch of useful info about the fortune.

```
w> /import [gen-fortune-2] from 'horoscope
w> gen-fortune-2 'Scorpio
[ #fortune api# \ 'fortune "." \ 'teller "Stacy O'Hara" \ 'told-on "09.06.2019" ]
w> gen-fortune-2 'Libra
[ #fortune api# \ 'error "Couldn't find a teller." ]
w> gen-fortune-2 'Cancer
[ #fortune api# \ 'fortune "Sleep soon." \ 'next [ \ "Seriously" ( \ "Go now." ())] ]
```

`gen-fortune-2` creates a monad.  It contains the fortune (or an error if the fortune couldn't be given), but its real usefulness is that it gives us context for what is going on - perhaps who made the fortune, are there others waiting after we're done with this one, etc.

## Retrofitting for monads

We've written a bunch of code that uses `gen-fortune`, and we want to use the snazzy new API, but we've got a problem: all of our code currently expects fortunes to be a string.  So we're going to have to modify the whole thing to work with functions instead of strings, and once that's done, we'll have to figure out what to do with all of this extra information.  Sounds painful!

Luckily, you already have everything you need to deal with monads.  Wall provides the function `monadize` to supercharge normal functions as monad-handling machines.  Assuming that `zodiac?` is a validator for Zodiac signs, let's say that we were consuming the API like this:

```
w> /import [gen-fortune zodiac?] from 'horoscope
w> my-gen-fortune = << zodiac? >>
  ? a0.== 'Cancer
  "Cancer is a premium sign, pay up!"
  $? a0. == 'Scorpio
  `Here's your horoscope: ${(gen-fortune a0)} and Leo too ${(gen-fortune 'Leo)}`
  (++ "Here is our prediction: " (gen-fortune a0))
w> my-gen-fortune 'Libra
"Here is our prediction: buy low, sell high!"
```

To use our new API, we simply sub `gen-fortune-2` for `gen-fortune` and use `monadize` to transform the function into something that handles our fortune monad.  Assuming the API provider provides a validator `fortune-2?`, we can write:

```
w> /import [gen-fortune zodiac? fortune-2?] from 'horoscope
w> fortune-merge = << function? fortune-2? fortune-2? >>
    ? (a1.has? 'error .| a2.has? 'error)
      { 'error [a1 a2].filter! k.has? 'error .map! k 'error }
      f+e (merge a0 a1) \ 'fortune (a0 a1 'fortune a2 'fortune)
w> my-gen-fortune = fortune-2? fortune-merge << zodiac? >>
  monadize (? a0.== 'Cancer
    "Cancer is a premium sign, pay up!"
    $? a0. == 'Scorpio
    `Here's your horoscope: ${(gen-fortune-2 a0)} and Leo too ${(gen-fortune-2 'Leo)}`
    (++ "Here is our prediction: " (gen-fortune-2 a0)))
```

## How `monadize` works

`monadize` and, more generally, any function that acts directly on a function's definition, acts like the aggregators we have seen so far with one major difference: they contain `evverrrythinggg` as their domain instead of `everything`.  As a result, they consume `[`, `(`, and `{` and produce something useful with them.  This is why we say Wall is a dialect of Lisp - it is possible to directly manipualte even the most complicated functions as if the were code.
