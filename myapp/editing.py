from PIL import Image, ImageOps
import numpy as np

def trim_image_to_square(image_file):
    """ trims whichever side of the image is longer to make the resulting image a square, and then grayscales it """
    width = image_file.image.width
    height = image_file.image.height
    if width < height:
        crop_from_top = (height - width) // 2
        image = Image.open(image_file)
        image = ImageOps.invert(image) # inverting the image to match the images of the sklearn dataset
        squared_gray = image.crop((0, crop_from_top, width, crop_from_top + width)).convert("L").resize((8, 8))
        arr_data = np.array(squared_gray)
    else:
        crop_from_left = (width - height) // 2
        image = Image.open(image_file)
        image = ImageOps.invert(image) # inverting the image
        squared_gray = image.crop((crop_from_left, 0, crop_from_left + height, height)).convert("L").resize((8, 8))
        arr_data = np.array(squared_gray)
    return arr_data / 255 # standardizing
