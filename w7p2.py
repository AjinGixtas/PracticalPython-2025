from PIL import Image
import numpy as np
from collections import Counter

img = Image.open("w7p2.png")
arr = np.array(img)
wire = arr.reshape(-1, 3)

unique, counts = np.unique(wire, axis=0, return_counts=True)

fTable = list(zip(unique, counts))
fTable.sort(key=lambda x: x[1])
fTable.reverse()
for e in fTable: print(e)
ans = ""
for i in range(3):
    r, g, b = fTable[i][0]
    word = f"{r:02X}{g:02X}{b:02X}"
    ans += word + " "
print(ans)