from PIL import Image
import numpy as np


def get_average_window_color(arr, height, width, window_height, window_width):
    return np.sum(arr[height: height + window_height,
                        width: width + window_width]) // (window_height * window_width * 3)


def replacement_pixels(arr, window_height, window_width, grayscale):
    for h in range(0, len(arr), window_height):
        for w in range(0, len(arr[1]), window_width):
            color = get_average_window_color(arr, h, w, window_height, window_width)
            color = int(color // grayscale) * grayscale
            arr[h: h + window_height, w: w + window_width] = np.full(3, color)

img = Image.open(input("введите название файла "))
arr = np.array(img)
window_height = int(input("введите высоту мозаики или будет использовано значение по умолчанию ") or "10")
window_width = int(input("введите ширину мозаики или будет использовано значение по умолчанию ") or "10")
grayscale = int(input("введите градацию серого или будет использовано значение по умолчанию ") or "50")
replacement_pixels(arr, window_height, window_width, grayscale)
res = Image.fromarray(arr)
print("complete")
res.save('res.jpg')
