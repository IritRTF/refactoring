from PIL import Image
import numpy as np


def do_mosaic(img, size, grey_size):
    for x in range(0, len(img), size):
        for y in range(0, len(img[0]), size):
            img[x:x + size, y:y + size] = find_average(
                img[x:x + size, y:y + size], size, grey_size)
    return img


def find_average(img_part, size, grey_size):
    average_color = (img_part[:size, :size].sum() / 3) // size ** 2
    return int(average_color // grey_size) * grey_size


np.seterr(over='ignore')
source_img = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
mosaic_size = int(input("Введите размер мозаики: "))
grey = int(input("Введите количество градаций серого: "))

img_code = np.array(source_img)
grey_size = 255 // grey

res = Image.fromarray(do_mosaic(img_code, mosaic_size, grey_size))
res.save(input("Введите имя файла, в которой хотите сохранить результат: "))
