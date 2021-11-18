from PIL import Image
import numpy as np

arr = np.array(Image.open(input('Введите название исходного изображения с расширением:')))
step, size = int(input('Введите количество шагов градации серого цвета:')), int(input('Введите размеры мозаики:'))
rows, columns = len(arr), len(arr[0])
for row in range(0, rows - size + 1, size):
    for col in range(0, columns - size + 1, size):
        mean = np.mean(arr[row:row + size, col:col + size])
        arr[row:row + size, col:col + size] = mean // step * step
res = Image.fromarray(arr)
res.save(input('Введите название результата (изображения) с расширением:'))
