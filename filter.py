from PIL import Image
import numpy as np
import os

def input_image():
    print('Введите название файла')
    s = input()
    while not os.listdir().__contains__(s):
        print('Такого файла нет, попробуйте еще раз')
        s = input()
    return s

def input_parametrs():
    print('Введите размер мозаики')
    size = int(input())
    print('Введите количество уровней градации ')
    step = int(255 // int(input()))
    return size, step


name = input_image()
size, step = input_parametrs()

img = Image.open(name)
arr = np.array(img)

i = 0
while i < len(arr):
    j = 0
    while j < len(arr[0]):
        s = np.mean(arr[i:i+size, j:j+size][:])
        arr[i:i+size, j:j+size][:] = int(s // step) * step
        j += size
    i += size

res = Image.fromarray(arr)
print('Введите название выходного файла (формат .jpg)')
res.save(input()+'.jpg')