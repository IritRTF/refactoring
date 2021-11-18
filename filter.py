import sys
from PIL import Image
import numpy as np


def median_gray(arr, grad_step):
    return int(np.sum(arr) // (len(arr) ** 2 * 3 * grad_step)) * grad_step


def gray_pixelation(image, pixel_size, gradations_count):
    grad_step = int(255 // (gradations_count - 1))
    arr = np.array(image)
    for i in range(0, len(arr) - pixel_size + 1, pixel_size):
        for j in range(0, len(arr[1]) - pixel_size + 1, pixel_size):
            res_color = median_gray(arr[i:i + pixel_size, j:j + pixel_size, 0:3], grad_step)
            arr[i:i + pixel_size, j:j + pixel_size, 0:3] = res_color
    return Image.fromarray(arr)


if __name__ == "__main__":
    gray_pixelation(Image.open(sys.argv[1]), 10, 5).save(sys.argv[2])
