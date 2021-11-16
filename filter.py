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



file_name = input("Введите имя файла который хотите преобразовать в мозаику: ")
res_name = input("Введите имя файла в который будет записан результат преобразования: ")
dimensions = [int(i) for i in input("Введите через запятую ширину и высоту одного элемента мозаики: ").split(',')]
gray_gradation = int(input("Введите число градаций серого: "))
img = Image.open(file_name)
img_arr = np.array(img)
transform_to_mosaic(img_arr, dimensions[0], dimensions[1], gray_gradation)
res = Image.fromarray(img_arr)
print("Преобразование завершено... Результат записан в файл: \"" + res_name + "\"")
res.save(res_name)