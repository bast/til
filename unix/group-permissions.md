# How to give group permission to read without making everything executable

```
$ chmod -R g+rX-w,o= /some/folder
```

The uppercase `X` is a "special execute", it applies execute permissions to
directories but makes files only group-executable if they are already
executable.
