from PIL import Image
import numpy as np


def replace_with_gray(width, height, arr, gradation):
    for x in range(0, len(arr), height):
        for y in range(0, len(arr[1]), width):

            grad = np.sum(arr[x: x + height, y: y + width]) // (height * width * 3)

            color = int(grad // gradation) * gradation
            arr[x: x + height, y: y + width] = np.full(3, color) #


img = Image.open("img2.jpg")
#img = Image.open(input("введите название файла "))

arr = np.array(img)

width = int(input('Введите ширину мозайки  '))
height = int(input('Введите высоту мозайки  '))
gradation = int(input('Введите градацию серого  '))

replace_with_gray(width, height, arr, gradation)

res = Image.fromarray(arr)
res.save('res.jpg')

