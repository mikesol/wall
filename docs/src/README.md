# Wall

This is the documentation for the Wall programming language.

## What is wall

Wall is a statically-typed language with inferred types, dependent types and duck typing. It features a compiler, a transpiler, an interpreter and plugins for various editors.

Wall is a good fit for programmers that work a lot with asynchronous IO and enjoy a functional style.  Its closest relatives are Scheme, TypeScript, F*, Idris and Haskell.


## Lazy, irritable and full of hubris

Larry Wall once famously said that programmers are "lazy, irritable and have a lot of hubris."  Wall is not exception.  In fact, laziness, irritability and hubris are its core feature set.  Let's explore each in further detail.

### Lazy

Wall is lazy, meaning that it won't evaluate anything until you absolutely need it.  A lot of ink has been spilled about the virtues and pitfalls of lazy languages.  While it is true that lazy algorithms have their disadvantages, in our opinion, the gains in expressivity outweigh these shortcomings.

In the Wall interpreter, every statement that you ask to be printed will be evaluated, whereas every statement stored in a variable will not.  If a statement is un-evaluatable because it would be too big, it reprints to the console.  The wall compiler, on the other hand, will throw a compile-time error for non-completing IO (ie writing an infinite object to a file or sending it over a network).

```
w> int
int
w> int ~ { 0 }
int ~ { 0 }
w> fil (< 0) int
fil (< 0) int
w> fil (< 0) (fil (> 2) int)
{ 1 }
```

### Irritable

Wall loves to complain.  IO of a recursive or infinitely-large `object` or `set`?  Error.  Key doesn't exist on an object?  Error.  Name already used?  Error.  You're trying to access something that is not an object?  Error. Actually, those are really the only four errors in Wall, but man does it throw a lot of them.  Lucky, editors like VS Code and Emacs make it easy to spot and correct these errors.

```
w> { 0 1 } 2
Error. The object { 0 1 } does not contain the key 2.
w> foo = 1
w> foo = 2
Error. Cannot rename foo = 1.
w> get `https://www.wall-lang.io/?q=${int}`
Error. Attempting to perform an IO operation with the infinitely-large set int.
w> z = { z }
w> get `https://www.wall-lang.io/?q=${z}`
Error. Attempting to perform an IO operation with the infinitely-large set z.
w> m = 1
w> m 'a
Error. m is not an object.
```

It is important to note that all these errors are *compile time*, not *runtime*.  One advantage of Wall is that it throws virtually no runtime errors, which means that once your code compiles, you can be virtually certain that it will work as intended.

### Hubris

Wall likes to steal the show.  As a result, it is pretty opinionated.  While this constrains the programmer somewhat, Wall creates conditions that allow for beautiful, clean, short programs with little room for ambiguity.  Programmers that enjoy impressing managers with 100s of lines of Java code to manage complex threading scenarios and IO heirarchies are disappointed by Wall's elegance and brevity.

