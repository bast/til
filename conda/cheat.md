# Conda cheat sheet

Reverses the init:
```
$ conda init --reverse
```

List all environments:
```
$ conda info -e
```

Get list of installed packages:
```
$ conda env list
```

Create a new environment:
```
$ conda create --name myenv
```

Activate a specific environment:
```
$ conda activate myenv
```

Deactivate current environment:
```
$ conda deactivate
```

Exports only actively installed packages:
```
$ conda export --from-history
```

Removing an environment:
```
$ conda remove --name myenv --all
```

To clean unnecessary cached files, tarballs, and stuff:
```
$ conda clean --all
```
