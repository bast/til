# Fun and bad way to figure out Python major version

Not to be used in any production but fun to reason about it. I got this from M.
B.:
```python
python_version = int(str(range(3))[-2])
```
