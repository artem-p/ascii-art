from PIL import Image
import numpy as np

BRIGHTNESS_MAX = 255
BRIGHTNESS_SYMBOLS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
BRIGHTNESS_SYMBOLS_COUNT = len(BRIGHTNESS_SYMBOLS)
BRIGHTNESS__TO_SYMBOL_SLOPE = BRIGHTNESS_SYMBOLS_COUNT / BRIGHTNESS_MAX


def to_brightness(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3


def brightness_to_symbol(brightness):
    return brightness * BRIGHTNESS__TO_SYMBOL_SLOPE

try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

# get image as 2d array
pixel_matrix = np.array(image)

# get single brightness value for pixel
brightness_matrix = list(map(lambda row: list(map(lambda pixel: to_brightness(pixel), row)), pixel_matrix))

# transform brightness to symbol
symbols_matrix = list(map(lambda row: list(map(lambda pixel: brightness_to_symbol(pixel), row)), brightness_matrix))

print(symbols_matrix)