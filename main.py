from PIL import Image
import numpy as np

def to_brightness(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3

try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

# get image as 2d array
pixel_matrix = np.array(image)

# get single brightness value for pixel
brightness_matrix = list(map(lambda row: list(map(lambda pixel: to_brightness(pixel), row)), pixel_matrix))

print(brightness_matrix)