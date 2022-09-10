# Sphinx container

```yaml
Bootstrap: docker
From: python:3.7-alpine

%files
    requirements.txt

%post
    apk add --no-cache build-base libffi-dev
    pip install --upgrade pip
    pip install -r requirements.txt

%environment
    export LC_ALL=C

%runscript
    sphinx-autobuild $@
```
