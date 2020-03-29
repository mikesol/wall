# Musings

Here are some random thoughts about Wall.

## Why I wrote Wall

The first languages in which I coded extensively are Scheme and Python.  I loved Scheme for its flexibility and functional style and Python for its simple imperative syntax.  Since then, I've worked on projects in C, C++, C#, Java, JavaScript, TypeScript, Swift, Kotlin, Groovy, Objective-C, Haskell, Erlang, Clojure, Elixir, Ruby, F# and other languages.

In doing so, I've learned a lot about how **static typing** can lead to a more pleasurable, bug-free coding experience that allows one to aggressively refactor due to the strength of the compiler. At the same time, the way one works with types never felt natural to me because, in most languages, it requires a meta-language on top of the language.  *I created Wall to explore a language where the compiler keeps track of functions' domains and ranges instead of types.*  While there's a lot left to explore, my hypothesis is that the rigorous accounting of domains and ranges allows for a higher level of expressiveness and type safety than languages like Haskell and Idris.