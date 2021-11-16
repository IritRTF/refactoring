from PIL import Image
import numpy as np


def pixel_brightness(arr, p_w, p_h, gr, i, j):
    brightness = np.sum(arr[i: i + p_h, j: j + p_w]) // (p_h * p_w * 3)
    brightness -= brightness % gr
    return brightness


def transform_to_mosaic(arr, p_w, p_h, gr):
    for i in range(0, len(arr), p_w):
        for j in range(0, len(arr[1]), p_h):
            brightness = pixel_brightness(arr, p_w, p_h, gr, i, j)
            arr[i: i + p_h, j: j + p_w] = np.full(3, brightness)


img = Image.open("img2.jpg")
img_arr = np.array(img)
pixel_height, pixel_width = 15, 15
gray_gradation = 10
transform_to_mosaic(img_arr, pixel_width, pixel_height, gray_gradation)
res = Image.fromarray(img_arr)
res.save('res.jpg')
