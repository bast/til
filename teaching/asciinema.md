# Recording terminal sessions with asciinema

[asciinema](https://asciinema.org/) is a very nice tool!

This starts and records a separate Bash session:
```bash
$ asciinema rec -c bash demo.cast
```

Convert to GIF:
```bash
$ agg demo.cast demo.gif
```
