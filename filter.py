

from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = np.sum(arr[i:i+10, j:j+10][0:2])
        s = int(s // 100)

        arr[i:i+10, j:j+10][:] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')