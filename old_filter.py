from PIL import Image
import numpy as np


def get_average(arr, x, y, size):
    sum = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            r = arr[i][j][0] // 3
            g = arr[i][j][1] // 3
            b = arr[i][j][2] // 3
            sum += r + g + b
    return int(sum // (size * size))


def replace_pixels(arr, x, y, size, value):
    for n in range(x, x + size):
        for m in range(y, y + size):
            arr[n][m][0] = value
            arr[n][m][1] = value
            arr[n][m][2] = value


def grayscale_image(arr, size, grayscale):
    height = len(arr)
    width = len(arr[1])

    for i in range(0, height, size):
        for j in range(0, width, size):
            avg = get_average(arr, i, j, size)
            replace_pixels(arr, i, j, size, int(avg // grayscale) * grayscale)


if __name__ == "__main__":
    arr = np.array(Image.open(input("Введите название файла: ")))
    size = int(input("Введите размер мозаики: "))
    grayscale = int(input("Введите градацию серого для мозаики: "))
    save_name = input("Введите название итогового файла: ")
    grayscale_image(arr, size, grayscale)

    res = Image.fromarray(arr)
    res.save(save_name)
