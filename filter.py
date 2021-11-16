from PIL import Image
import numpy as np


def write_pixel(x, y, arr, pixel_size, color_step):
    grey_average = np.mean(arr[x:x+pixel_size, y:y+pixel_size][:])
    color = int(grey_average // color_step) * color_step
    arr[x:x+pixel_size,y:y+pixel_size][:] = color

def main():
    name_in_file, name_out_file = input().split(' ')
    img = Image.open(name_in_file)
    arr = np.array(img)
    img_width = len(arr)
    img_height = len(arr[0])
    gradations = 5
    color_step = 255 // gradations
    pixel_size = 10
    for x in range(0, img_width - pixel_size + 1, pixel_size):
        for y in range(0, img_height - pixel_size + 1, pixel_size):
            write_pixel(x, y, arr, pixel_size, color_step)
    res = Image.fromarray(arr)
    res.save(name_out_file)

main()
