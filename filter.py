from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)

i = 0
while i < len(arr):
    j = 0
    while j < len(arr[0]):
        s = np.mean(arr[i:i+10, j:j+10][:])
        arr[i:i+10, j:j+10][:] = int(s // 50) * 50
        j += 10
    i += 10

res = Image.fromarray(arr)
res.save('res.jpg')