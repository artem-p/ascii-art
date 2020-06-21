from PIL import Image
import numpy as np

BRIGHTNESS_MAX = 255
BRIGHTNESS_SYMBOLS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
BRIGHTNESS_SYMBOLS_COUNT = len(BRIGHTNESS_SYMBOLS)
BRIGHTNESS__TO_SYMBOL_SLOPE = BRIGHTNESS_SYMBOLS_COUNT / BRIGHTNESS_MAX


def to_brightness(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3


def pixel_to_symbol(pixel):
    # get single brightness value for pixel
    brightness = to_brightness(pixel)

    symbol_position = round(brightness * BRIGHTNESS__TO_SYMBOL_SLOPE)

    if 0 <= symbol_position <= BRIGHTNESS_SYMBOLS_COUNT:
        return BRIGHTNESS_SYMBOLS[symbol_position] * 2 # double symbols so image doesn't look squashed
    else:    
        return ''


def scale_image(image, new_width=250):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

# scale image so you can display it
image = scale_image(image)

# get image as 2d array
pixel_matrix = np.array(image)


# transform pixel to symbol
symbols_matrix = list(map(lambda row: list(map(lambda pixel: pixel_to_symbol(pixel), row)), pixel_matrix))

ascii_art = '\n'.join(''.join(str(symbol) for symbol in row) for row in symbols_matrix)
print(ascii_art)

output_file_path = 'output.txt'

output_file = open(output_file_path, 'w')

output_file.write(ascii_art)
