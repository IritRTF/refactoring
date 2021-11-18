from PIL import Image
import numpy as np


def change(x, y, arr, len, step):
    bright_avg = np.average(arr[x: x + len, y: y + len][:])
    arr[x: x + len, y: y + len][:] = int(bright_avg // step) * step


def get_mosaic(arr, size, step):
    new_arr = arr
    for x in range(0, width - size + 1, size):
        for y in range(0, height - size + 1, size):
            change(x, y, new_arr, size, step)
    return new_arr


open_name = input('Введите полный путь до изображения : ')
fin_name = input('Введите имя выходного изображения : ')
img = Image.open(open_name)

array = np.array(img)

size = int(input('Введите длину стороны мозайки'))
gr = int(input('Введите градацию серого цвета'))

width = len(array)
height = len(array[1])
step = 255 // gr

res = Image.fromarray(get_mosaic(array, size, step))
res.save(fin_name)
