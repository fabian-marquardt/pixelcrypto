from math import floor
from PIL import Image


class ImageMalformedException(Exception):
    pass


def get_pixel_byte(pixel):
    character_value = 0
    for val in pixel:
        if character_value == 0:
            character_value = val
        elif val != 0 and character_value != val:
            raise ImageMalformedException("This image is not a valid pixelcrypto image!")
    return bytes([character_value])


def decode(filename, pixel_width=16, pixel_height=16):
    img = Image.open(filename).convert('RGB')
    characters = floor(img.width / pixel_width)
    byte_array = b''
    for i in range(0, characters-1):
        pixel = img.getpixel((i*pixel_width + pixel_width/2, pixel_height / 2))
        byte_array += get_pixel_byte(pixel)
    return byte_array


if __name__ == '__main__':
    print(decode("test1.png").decode('utf-8'))
    print(decode("test2.png").decode('utf-8'))
    print(decode("test3.png").decode('utf-8'))
    print(decode("test4.png").decode('utf-8'))
    print(decode("test5.png").decode('utf-8'))
    print(decode("test6.png").decode('utf-8'))