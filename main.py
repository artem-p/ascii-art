from PIL import Image

try:
    image = Image.open('sample-image.jpg')
except IOError as error:
    print('Cannot load image')

print('Successfully loaded image!')

print('Image size: ' + str(image.size[0]) + ' x ' + str(image.size[1]))