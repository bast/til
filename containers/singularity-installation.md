# How to install Singularity

Requires sudo in last step.
Also requires Go installed and in `$PATH`.

```
#!/usr/bin/env bash

export VERSION=3.7.1

wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz

tar -xzf singularity-${VERSION}.tar.gz

cd singularity

./mconfig
make -C builddir
sudo make -C builddir install
```

See also https://sylabs.io/guides/3.5/user-guide/quick_start.html#compile.
