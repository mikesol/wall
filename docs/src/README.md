# Wall

This is the documentation for the Wall programming language.

## What is Wall?

Wall is a dialect of Lisp whose compiler uses **function domain verification** (FDV) instead of **static type checking** to enforce the correctness of programs. In FDV, the compiler keeps track of functions' potential domains at _compile time_, raising an error if a function is invoked with a value that is potentially outside of its domain.

Wall's closest relatives from the Lisp family are Scheme and Clojure, but it also takes inspiration from TypeScript, F\*, Idris, Haskell, Erlang and Lua.

## What is this document?

This document provides a gentle introduction to Wall. We recommend reading it sequentially. To learn more about the motivation behind Wall and how it works under the hood, you can skip directly to the last chapter, [Musings](./musings).
