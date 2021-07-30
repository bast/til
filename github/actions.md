# Trick to use env vars in GH Action workflows

```yaml
- name: Location of Conda
    shell: bash
    run: |
    if [ "${{ matrix.os }}" == "windows-latest" ]
      then echo "BIN=Scripts" >> $GITHUB_ENV
      else echo "BIN=bin" >> $GITHUB_ENV
    fi
```
