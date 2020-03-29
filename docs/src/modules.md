# Modules

Modules in Wall work like languages like Haskell.  Functions can be exported using `export` and imported using `import`.

For example, we can export two functions from the module `my-math.wall`.

```
// my-math.wall
add-5 = + 5
times-2 = * 2
\export [add-5 times-2]
```

And then import them like so:

```
w> \import { add-5, times-2 } 'my-math
w> add-5 3
8
```

In case you want to rename a function, you can modify the function in the import:

```
w> \import { add-5: awesome-5-adder, times-2 } 'my-math
w> awesome-5-adder 3
8
```
