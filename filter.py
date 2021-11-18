import sys
from PIL import Image
import numpy as np


def median_gray(arr, step):
    return int(np.mean(arr) // step) * step


def gray_pixelation(image, size, gradations):
    step = int(255 // (gradations - 1))
    arr = np.array(image)
    for row in range(0, len(arr) - size + 1, size):
        for column in range(0, len(arr[1]) - size + 1, size):
            arr[row:row + size, column:column + size] = \
                median_gray(arr[row:row + size, column:column + size], step)
    return Image.fromarray(arr)


if __name__ == "__main__":
    gray_pixelation(Image.open(sys.argv[1]), 10, 5).save(sys.argv[2])
