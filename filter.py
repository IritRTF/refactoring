from PIL import Image
import numpy as np


def get_average_window_color(arr, height, width, window_height, window_width):
    return np.sum(arr[height: height + window_height,
                        width: width + window_width]) // (window_height * window_width * 3)
#    for n in range(height, height + filter_frequency):
#        for m in range(width, width + filter_frequency):
#            r = arr[n][m][0]
#            g = arr[n][m][1]
#            b = arr[n][m][2]
#            M = r // 3 + g // 3 + b // 3
#            sum_window += M
#    return int(sum_window // (filter_frequency * filter_frequency))


def replacement_pixels(arr, window_height, window_width, grayscale):
    for h in range(0, len(arr), window_height):
        for w in range(0, len(arr[1]), window_height):
            color = get_average_window_color(arr, h, w, window_height, window_width)
            color = int(color // grayscale) * grayscale
            arr[h: h + window_height, w: w + window_width] = np.full(3, color)


img = Image.open("img2.jpg")
arr = np.array(img)
height = len(arr)
width = len(arr[1])
window_height = 5
window_width = 5
grayscale = 10
replacement_pixels(arr, window_height, window_width, grayscale)
res = Image.fromarray(arr)
res.save('res.jpg')
