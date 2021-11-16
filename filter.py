from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i <= a - 10:
    j = 0
    while j <= a1 - 10:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                n1 = arr[n][n1][0]
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = (int(n1) + int(n2) + int(n3))/3
                s += M
        c = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(c // 50) * 50
                arr[n][n1][1] = int(c // 50) * 50
                arr[n][n1][2] = int(c // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
