# Threading

Wall, like Node.js, has an opinionated view on threading that is not possible to change without fiddling with compiler options or messing around with internals.  That said, we think it provides a sensible default for all but the most esoteric cases.

Because the topology of a Wall program is known at compile time, for an isolated Wall program that has no side effects (ie no calls to the file system, no )