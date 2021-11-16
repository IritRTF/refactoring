from PIL import Image
import numpy as np

np.seterr(over='ignore')

def find_average_brightness(x_idx, y_idx, size, array):
    s = 0
    for x in range(x_idx, x_idx + size):
        for y in range(y_idx, y_idx + size):
            n1 = array[x][y][0] / 3
            n2 = array[x][y][1] / 3
            n3 = array[x][y][2] / 3
            M = n1 + n2 + n3
            s += M
    return int(s // (size * size))


def transform_to_mosaic(x_idx, y_idx, arr, size, step, average_brightness):
    for x in range(x_idx, x_idx + size):
        for y in range(y_idx, y_idx + size):
            arr[x][y][0] = int(average_brightness // step) * step
            arr[x][y][1] = int(average_brightness // step) * step
            arr[x][y][2] = int(average_brightness // step) * step


img = Image.open("img2.jpg")
arr = np.array(img)

size = int(input('Введите длину боковой стороны мозайки (например: 10 (x*x)) : '))
gradation = int(input('Введите градацию серого (например: 5) : '))
step = 255 // gradation

width = len(arr)
height = len(arr[1])

for x in range(0, width - size + 1, size):
    for y in range(0, height - size + 1, size):
        transform_to_mosaic(x, y, arr, size, step, find_average_brightness(x, y, size, arr))
res = Image.fromarray(arr)
res.save('res.jpg')
