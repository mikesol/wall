# Anatomy

Let's make a file called `hello-world.wall` and put the following bit of Wall code.  Don't worry for now what it does, just take it on faith that this is correct syntax.

```
#Hello, world!# =
#Hello, world!#
```

Now, from the command line or from the Wall Online Interpreter, run `wall hello-world.wall`. You should see the following result:

```
Hello, world!
```

And there we have it.  Hello world in Wall.

## Compiler

Informally a Wall program has a bunch of stuff written sequentially in a file separated by newlines.  If the last line is not an [Assignment](#Assignment), it will return the value of the last line.

The Wall compiler, called `wall`, reads a Wall program and prints the result to standard out.

## Interpreter

For the remainder of the exercises in this guide, we will write them as if they are using the Wall interpreter.  The Wall interpreter can be invoked by typing `wall` on the command line.  The same example above can be accomplished as follows:

```
w> #Hello, world!# =
w> #Hello, world!#
Hello, world!
```
