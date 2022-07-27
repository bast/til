# Maturin and test-PyPI

```
- name: Maturin publish
  run:
    maturin publish --no-sdist -r https://test.pypi.org/legacy/ -u __token__ -i python --cargo-extra-args="--features pyo3"
  env:
    MATURIN_PASSWORD: ${{ secrets.PYPI_TOKEN }}
```
