from PIL import Image
import numpy as np

img = Image.open("w5p2.png")
arr = np.array(img)

# Flatten image into a wire of pixels
if arr.ndim == 3:
    wire = arr.reshape(-1, arr.shape[-1])
    channels = arr.shape[-1]
else:
    wire = arr.ravel()
    channels = None
dimension = int(np.sqrt(len(wire)))

if channels: new_arr = np.zeros((dimension, dimension, channels), dtype=np.uint8)
else: new_arr = np.zeros((dimension, dimension), dtype=np.uint8)

idx = 0

for diag in range(2 * dimension - 1):
    coords = []
    row_start = max(0, diag - dimension + 1)
    row_end = min(diag + 1, dimension)
    for row in range(row_start, row_end):
        col = diag - row
        coords.append((row, col))
    if diag % 2 == 0: coords.reverse()
    for y, x in coords:
        if idx >= len(wire): break

        new_arr[y, x] = wire[idx]
        idx += 1

Image.fromarray(new_arr).save("w5p2-A.png")