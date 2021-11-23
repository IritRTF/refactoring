import os
import numpy as np
from PIL import Image, UnidentifiedImageError


def load_img(path: str):
    if os.path.isfile(path):
        try:
            img = Image.open(path)
            return np.array(img)
        except UnidentifiedImageError:
            raise TypeError("Incorrect file type.")
    raise FileExistsError("This file doesn't exist.")


def convert_to_gray_pixel_art(img: np.ndarray, pixel_size: int = 10, grayscale: int = 50):
    width = len(img)
    height = len(img[1])

    for x in range(0, width, pixel_size):
        for y in range(0, height, pixel_size):
            brightness = 0
            for x1 in range(x, min(x + pixel_size, width)):
                for y1 in range(y, min(y + pixel_size, height)):
                    brightness += sum(int(color) for color in img[x1][y1]) // 3
            brightness = brightness // (pixel_size * pixel_size)

            for x1 in range(x, min(x + pixel_size, width)):
                for y1 in range(y, min(y + pixel_size, height)):
                    img[x1][y1][0] = img[x1][y1][1] = img[x1][y1][2] = brightness - brightness % grayscale
    return img


def save_img(img: np.ndarray, filename: str):
    Image.fromarray(img).save(filename)


def main():
    img = load_img("img2.jpg")
    gray_image = convert_to_gray_pixel_art(img, 10, 50)
    save_img(gray_image, "res.jpg")


if __name__ == "__main__":
    main()