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
while i <= a - 10:
    j = 0
    while j <= a1 - 10:
        s = 0
        for x_axis in range(i, i + 10):
            for y_axis in range(j, j + 10):
                red = arr[x_axis][y_axis][0]
                green = arr[x_axis][y_axis][1]
                blue = arr[x_axis][y_axis][2]
                M = (int(red) + int(green) + int(blue)) // 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for y_axis in range(j, j + 10):
                arr[n][y_axis][0] = int(s // STEPS) * STEPS
                arr[n][y_axis][1] = int(s // STEPS) * STEPS
                arr[n][y_axis][2] = int(s // STEPS) * STEPS
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
