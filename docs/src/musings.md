# Random Musings

## Sets and `set`-s

Programming languages are allergic to sets.  In a language like C, there is no elegant way to refer to a collection of objects without somehow encoding their sequence, ie an array or a struct.  In languages Reason, the Variant resembles a Set whose contents are known at compile time, but it is difficult to construct a runtime set without using an external library.

In Wall, `set`-s are first-class citizens. Without knowing the set that represents the keys of an `object` (ie `int`), it would be impossible to do compile-time type checking.  Under the hood, this requires a lot of duct tape and pixie dust, but for programmers, we hope this provides a smooth and elegant abstract to get things done fast.

## Lists and `set`-s

Wall contains a predefined immutable list construct because we haven't yet figured out what a list *is*, and we are too chicken to hazard a guess.  As we've seen before, there are two ways to create a list-like structure: an object indexed by successive integers starting at 0 and linked list composed of nested objects.  Both accomplish different goals, and you can use whichever one fits your use case better.

Or better yet, why not just use a set?  How often do you really, really need a list?  Usually, you just have a bag of stuff to which you want to apply some sort of ordering.  Outside of the context of the ordering, are things *really* ordered?  Like the houses on my street - I can order them in terms of their address, their size, the number of people inside, etc.  But outside of the scope of these orderings, do these houses really have some inherent quality of order-ness that needs to be encoded in a list?  No, it's just a set of houses that happen to have the quality "on my street."

Of course, a lot of times you need to work with ordered lists because certain IO formats, like `json` and `yaml`, contain ordered lists.  In this case, it is easy to represent these formats by using objects.

## Proofs

If you've worked with languages like Coq or F*, you have probably surmised by now that Wall uses an automatic proof assistant to verify set inclusion and equality.
The most important question the Wall compiler asks is "is `x` a subset of `y`".

For example, let's define the Mandelbrot set.

```
w> mandelbrot'0 = omap! complex { k 0+0i }
w> mandelbrot = mandelbrot'0
  .map! { k { v { (+ (sq ..k) k) . } } }
  .fil! $== +inf a.end.choose
  .key
w> in? 0+0j mandelbrot
true
```
Wall is able to do this because, under the hood, it uses several

## Native `set`-s