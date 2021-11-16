from PIL import Image
import numpy as np


def find_median(img_code, x, y):
    n1 = img_code[x][y][0] / 3
    n2 = img_code[x][y][1] / 3
    n3 = img_code[x][y][2] / 3
    median = n1 + n2 + n3
    return median


np.seterr(over='ignore')
source_img = Image.open("img2.jpg")
img_code = np.array(source_img)
count_x = len(img_code)
count_y = len(img_code[1])

print("Введите размер мозаики: \n(Рекомендуемый размер мозаики - 10, "
      "возможные значения - 1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 125, 150, 250, 375, 750)")
mosaic_size = int(input())
print("Введите, насколько будет детализировано изображение от 1 до 100. 1 - высокая детализация, 100 - низкая: ")
grey = int(input())

i = 0
while i < count_x:
    j = 0
    while j < count_y:
        sum_m = 0
        for x in range(i, i + mosaic_size):
            for y in range(j, j + mosaic_size):
                sum_m += find_median(img_code, x, y)
        sum_m = int(sum_m // 100)
        for k in range(i, i + mosaic_size):
            for m in range(j, j + mosaic_size):
                img_code[k][m][0] = int(sum_m // grey) * grey
                img_code[k][m][1] = int(sum_m // grey) * grey
                img_code[k][m][2] = int(sum_m // grey) * grey
        j = j + mosaic_size
    i = i + mosaic_size
result = Image.fromarray(img_code)
result.save('res.jpg')
