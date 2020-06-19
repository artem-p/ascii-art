from PIL import Image
import numpy as np

try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

image_array = np.array(image)

print(image_array)