from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)

print('Введите размер мозаики')
size = int(input())
print('Введите количество уровней градации ')
step = int(255 // int(input()))

i = 0
while i < len(arr):
    j = 0
    while j < len(arr[0]):
        s = np.mean(arr[i:i+size, j:j+size][:])
        arr[i:i+size, j:j+size][:] = int(s // step) * step
        j += size
    i += size

res = Image.fromarray(arr)
res.save('res.jpg')