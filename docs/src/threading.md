# Threading

Wall, like Node.js, has an opinionated view on threading that is not possible to change without fiddling with compiler options or messing around with internals.  That said, we think it provides a sensible default for all but the most esoteric cases.

Like Haskell, Wall is lazy.  Wall's compiler then attempts to optimally distribute operations to a thread pool whose size is based on the `--thread-pool-size` argument passed to the compiler. IO operations are treated differently.  If the Wall compiler determines that a code path will trigger an IO operation with 100% certainty, it will do an eager evaluation of the IO operation.