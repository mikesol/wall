# Packages

The Wall package manager, Bricks, is automatically installed with Wall.  You can use it to import your favorite wall packages into your toplevel Wall project.  Bricks is a simple Wall script that checks out a git project and creates a simple file, not unlike `yarn.lock` in `yarn`, that takes care of versioning of packages and should be checked into version control.

```
$ bricks init -y
$ bricks https://github.com/mikesol/wall-server
$ git add bricks.yml bricks.lock
```

Now, you can use anything from `wall-server` in your Wall project or from the Wall interpreter.

```
w> \import ['serve] 'wall-server
w> serve { 'port 8000 'routes { 'hello 'world } }
"Serving on port 8000"
```

Now, let's ping our server

```
$ curl localhost:8000/hello
world
```