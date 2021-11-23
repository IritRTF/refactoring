from PIL import Image
import numpy as np

def get_color (x, y, size_of_part, array):
    shade = 0
    for i in range(x, x + size_of_part):
        for j in range(y, y + size_of_part):
            red = arr[i][j][0]
            green = arr[i][j][1]
            blue = arr[i][j][2]
            col_pix = (int(red) + int(green) + int(blue))
            shade += col_pix
            return shade
            

img = Image.open("img2.jpg")
arr = np.array(img)
STEPS = 50
SIZE = 10
width = len(arr)
height = len(arr[1])
i = 0
while i < width - SIZE - 1:
    j = 0
    while j < height - SIZE - 1:
        shade = int(get_color(i, j, SIZE, arr) / 3 // SIZE ** 2)
        for x_axis in range(i, i + SIZE):
            for y_axis in range(j, j + SIZE):
                arr[x_axis][y_axis][0] = int(s // STEPS) * STEPS
                arr[x_axis][y_axis][1] = int(s // STEPS) * STEPS
                arr[x_axis][y_axis][2] = int(s // STEPS) * STEPS
        j = j + SIZE
    i = i + SIZE
res = Image.fromarray(arr)
res.save('res.jpg')
