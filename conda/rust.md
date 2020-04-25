

# Building a Rust project with Conda

Inspired by https://github.com/conda-forge/ripgrep-feedstock/tree/master/recipe.

First install `conda-build`:
```
$ conda install conda-build
```

Create at least two files under `/home/someuser/myproject`:

`build.sh`:
```bash
#!/usr/bin/env bash

set -o xtrace -o nounset -o pipefail -o errexit

# build statically linked binary with Rust
cargo install --locked --root "$PREFIX" --path .

# strip debug symbols
"$STRIP" "$PREFIX/bin/myproject"

# remove extra build file
rm -f "${PREFIX}/.crates.toml"
```

`meta.yaml`:
```yaml
{% set version = "0.1.0" %}

package:
  name: myproject
  version: {{ version }}

source:
  url: https://github.com/someuser/myproject/archive/{{ version }}.tar.gz
  sha256: d8ceef347b07b8de1675950ec917bf4f5432d189c952d8b415e5d5470bc6c008

build:
  number: 1

requirements:
  build:
    - rust
    - {{ compiler('c') }}        # [not win]
    - {{ compiler('m2w64_c') }}  # [win]

test:
  commands:
    - myproject --help

about:
  home: https://github.com/someuser/myproject
  license: GPL-3.0
  summary: One-line description of your project in here.
  license_file: LICENSE

extra:
  recipe-maintainers:
    - someuser
```

After you have created these files, build your project:
```
$ conda build /home/someuser/myproject
```

Towards the end of output from `conda build /home/someuser/myproject` you will see:
```
# Automatic uploading is disabled
# If you want to upload package(s) to anaconda.org later, type:

anaconda upload /home/someuser/miniconda3/envs/myenv/conda-bld/linux-64/myproject-0.1.0-h14c3975_1.tar.bz2
```

Finally install the project into your current environment:
```
$ conda install /home/someuser/miniconda3/envs/myenv/conda-bld/linux-64/myproject-0.1.0-h14c3975_1.tar.bz2
```
