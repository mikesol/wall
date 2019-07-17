# Threading

Wall, like Node.js, has an opinionated view on threading that is not possible to change without fiddling with compiler options or messing around with internals.  That said, we think it provides a sensible default for all but the most esoteric cases.

Like Haskell, Wall is lazy.  Wall will defer computation of anything until it is explicitly needed, which is what makes it possible to work with objects that are infinitely broad and infinitely deep.  At the same time, a Wall program with no IO or randomness is completely deterministic.  So the compiler knows after a first pass what (lazy) operations will be performed.  Wall's compiler then farms these operations out to a thread pool whose size is based on the `--thread-pool-size` argument passed to the compiler.

In the case of IO operations, things are a bit different.  The Wall compiler assumes that all IO operations will succeed and continues processing all code that represents the "happy path."  If the IO operation fails, Wall will terminate the execution of that code and go down the unhappy path.