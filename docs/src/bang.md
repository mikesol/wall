# Bang

Sometimes, you need Wall to evaluate something. Now. Wall's evaluation is lazy by default, but you can change this behavior by using the bang operator `!`. Like in Haskell, putting `!` before any element causes it to evaluate *now*.  While this may not seem useful as everything evaluates immediately in the Wall interpreter, we will see this shine in the next section about indeterminacy.