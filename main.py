from PIL import Image
import numpy as np

try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

# get image as 2d array
pixel_matrix = np.array(image)

for x in len(pixel_matrix):
    for y in len(pixel_matrix[x]):
        pixel = pixel_matrix[x][y]

        print(pixel)
