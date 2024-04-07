# Sorting values into bins using bisect

```python
import bisect
from collections import defaultdict


bins = [0, 10, 20, 30]
numbers = [5, 7.7, 10, 25, 1, 15, 32]


sorted_bins = defaultdict(list)
for number in numbers:
    index = bisect.bisect_right(bins, number) - 1
    sorted_bins[index].append(number)


print(sorted_bins)
```
