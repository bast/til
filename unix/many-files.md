# Creating many small files

```bash
#!/usr/bin/env bash

dd if=/dev/urandom of=bigfile bs=1 count=100000
split -b 10 -a 10 bigfile
```
