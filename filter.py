from PIL import Image
import numpy as np


def get_average_window_color(arr, height, width, filter_frequency):
    sum_window = 0
    for n in range(height, height + filter_frequency):
        for m in range(width, width + filter_frequency):
            r = arr[n][m][0]
            g = arr[n][m][1]
            b = arr[n][m][2]
            M = r // 3 + g // 3 + b // 3
            sum_window += M
    return int(sum_window // (filter_frequency * filter_frequency))


def replacement_pixels(arr, height, width, filter_frequency, grayscale, color):
    for n in range(height, height + filter_frequency):
        for n1 in range(width, width + filter_frequency):
            arr[n][n1][0] = int(color // grayscale) * grayscale
            arr[n][n1][1] = int(color // grayscale) * grayscale
            arr[n][n1][2] = int(color // grayscale) * grayscale


img = Image.open("img2.jpg")
arr = np.array(img)
height = len(arr)
width = len(arr[1])
filter_frequency = 10
grayscale = 50
window_height = 0
while window_height < height:
    window_width = 0
    while window_width < width:
        color_pixel = get_average_window_color(arr, window_height, window_width, filter_frequency)
        replacement_pixels(arr,
                           window_height,
                           window_width,
                           filter_frequency,
                           grayscale,
                           get_average_window_color(arr, window_height, window_width, filter_frequency))
        window_width = window_width + filter_frequency
    window_height = window_height + filter_frequency
res = Image.fromarray(arr)
res.save('res.jpg')
