from PIL import Image
import numpy as np


def calc_grey_average(x_idx, x_length, y_idx, y_length, array):
    total = 0
    for x in range(x_idx, x_idx + x_length):
        for y in range(y_idx, y_idx + y_length):
            red = array[x][y][0]
            green = array[x][y][1]
            blue = array[x][y][2]
            mean = (int(red) + int(green) + int(blue)) / 3
            total += mean
    return int(total // (x_length * y_length))


def write_pixels(x_idx, y_idx, out_arr, pixel_size, color_step, grey_average):
    color = int(grey_average // color_step) * color_step
    for x in range(x_idx, x_idx + pixel_size):
        for y in range(y_idx, y_idx + pixel_size):
            out_arr[x][y][0] = color
            out_arr[x][y][1] = color
            out_arr[x][y][2] = color


img = Image.open("img2.jpg")
arr = np.array(img)
gradations = 5
color_step = 255 // gradations
pixel_size = 10
img_width = len(arr)
img_height = len(arr[1])
for x in range(0, img_width - pixel_size + 1, pixel_size):
    for y in range(0, img_height - pixel_size + 1, pixel_size):
        write_pixels(x,
                     y,
                     arr,
                     pixel_size,
                     color_step,
                     calc_grey_average(x, pixel_size, y, pixel_size, arr))
res = Image.fromarray(arr)
res.save('res.jpg')
