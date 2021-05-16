from PIL import Image
import numpy as np
from settings import win_height,win_width
import matplotlib.pyplot as plt


def process_image(path):
    """
    returns numpy array from resized image
    :param path:
    :param length:
    :return: ndarray
    """
    # Open and fit to map
    img = Image.open(path)
    width, height = img.size
    img = img.resize((win_width, win_height), Image.BICUBIC)
    # Convert to black and white
    thresh = 170
    fn = lambda x: 255 if x > thresh else 0
    img = img.convert('L').point(fn, mode='1')
    img.save("cleaned.png")
    return np.array(img)


if __name__ == '__main__':
    pass