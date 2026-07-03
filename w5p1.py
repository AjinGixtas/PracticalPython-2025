from PIL import Image
import numpy as np

img = Image.open("w5p1.png")
arr = np.array(img)

flat = arr.reshape(-1, arr.shape[-1]) if arr.ndim == 3 else arr.ravel()

dimension = int(np.sqrt(flat.shape[0]))
flat = flat[:dimension * dimension]

new_arr = flat.reshape(dimension, dimension, -1) if arr.ndim == 3 else flat.reshape(dimension, dimension)

Image.fromarray(new_arr.astype(np.uint8)).save("w5p1-A.png")