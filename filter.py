from PIL import Image
import numpy as np

def get_color ()

img = Image.open("img2.jpg")
arr = np.array(img)
STEPS = 50
SIZE = 10
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - SIZE - 1:
    j = 0
    while j < a1 - SIZE - 1:
        s = 0
        for x_axis in range(i, i + SIZE):
            for y_axis in range(j, j + SIZE):
                red = arr[x_axis][y_axis][0]
                green = arr[x_axis][y_axis][1]
                blue = arr[x_axis][y_axis][2]
                M = (int(red) + int(green) + int(blue))
                s += M
        s = int(s / 3 // SIZE ** 2)
        for x_axis in range(i, i + SIZE):
            for y_axis in range(j, j + SIZE):
                arr[x_axis][y_axis][0] = int(s // STEPS) * STEPS
                arr[x_axis][y_axis][1] = int(s // STEPS) * STEPS
                arr[x_axis][y_axis][2] = int(s // STEPS) * STEPS
        j = j + SIZE
    i = i + SIZE
res = Image.fromarray(arr)
res.save('res.jpg')
