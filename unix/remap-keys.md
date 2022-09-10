# How to remap keys

My "Up" key broke off and here I remap "Up" to "PgUp":

```bash
#!/usr/bin/env bash

xmodmap -e "keycode 112 = Up"
```

See also: https://ictsolved.github.io/remap-key-in-linux/
