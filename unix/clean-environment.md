# How to run a command in a clean environment

```
$ env -i somecommand
```

For instance you can try this:
```bash
$ env         # prints all environment variables
$ env -i env  # should print nothing
```
