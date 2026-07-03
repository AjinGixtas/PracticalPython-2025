import re
with open("w7p1.inp", "r", encoding="utf-8") as f: data = f.readline().strip()
from collections import Counter

counts = Counter(data[i:i+4] for i in range(len(data) - 3))
for pattern, count in counts.items():
    if count == 1081: print(pattern)
    if count == 1055: print(pattern)
    if count == 965: print(pattern)