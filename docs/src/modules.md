# Modules

Modules in Wall work like languages like Haskell.  Functions can be exported using `export` and imported using `import`.

```
// exportables.wall
foo = <<! _? >> a0
bar = <<! boolean? >> not a0
\export [foo bar]
```

```
// importables.wall
\import ['foo 'bar] 'exportables
foo (bar true)
```

```
$ wall importables.wall
false
```
In case you want to rename a function, you can use a pair in import:


```
// exportables.wall
foo = <<! _? >> a0
bar = <<! boolean? >> not a0
\export [foo bar]
```

```
// importables.wall
\import ['foo \ 'bar 'baz] 'exportables
foo (baz true)
```

```
$ wall importables.wall
false
```