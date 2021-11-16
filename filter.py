from PIL import Image
import numpy as np

np.seterr(over='ignore')


def transform_to_mosaic(x, y, arr, size, step):
    average_brightness = np.mean(arr[x:x+size, y:y+size][:])
    arr[x:x+size, y:y+size][:] = int(average_brightness // step) * step

img = Image.open("img2.jpg")
arr = np.array(img)

size = int(input('Введите длину боковой стороны мозайки (например: 10 (x*x)) : '))
gradation = int(input('Введите градацию серого (например: 5) : '))
step = 255 // gradation

width = len(arr)
height = len(arr[1])

for x in range(0, width - size + 1, size):
    for y in range(0, height - size + 1, size):
        transform_to_mosaic(x, y, arr, size, step)
res = Image.fromarray(arr)
res.save('res.jpg')
