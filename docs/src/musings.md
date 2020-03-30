# Musings

Here are some random thoughts about Wall.

## Why I wrote Wall

The first languages in which I coded extensively are Scheme and Python.  I loved Scheme for its flexibility and functional style and Python for its simple imperative syntax.  Since then, I've worked on projects in C, C++, C#, Java, JavaScript, TypeScript, Swift, Kotlin, Groovy, Objective-C, Haskell, Erlang, Clojure, Elixir, Ruby, F# and other languages.

In doing so, I've learned a lot about how **static typing** can lead to a more pleasurable, bug-free coding experience. At the same time, types never felt natural to me because, in most languages, they require a meta-language on top of the language.  *I created Wall to explore a language where the compiler keeps track of functions' domains instead of types.* This eliminates the need for a meta-language to describe types, kinds, and higher-kinded types, instead only verifying that a function is never invoked with a value that is potentially outside of its domain. I'm sure someone smarter than me has come up with a name for this, but because I can't find it, I've coined the term *function domain verification*, or FDV.

While there's a lot left to explore, my hypothesis is that the rigorous verification of functions' domains allows for a higher level of expressiveness and type safety than languages like Haskell and Idris.