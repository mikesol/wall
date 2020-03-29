# Strings

In Wall, strings can be created three different ways:

```
w> a = 'aString
w> print a
aString
w> b = "a\tString"
w> print b
a    String
w> c = `${a}
${b}`
w> print c
aString
a    String
```

Byte strings are created by prepending `b` to the string. In this case, the string must be defined with double quotation marks.

```
w> a = b"hello"
```