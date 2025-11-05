# Function to load an image from file path
# Function to display image in a window
from cv2 import imread, IMREAD_COLOR


def load_image(img_name, color_type=IMREAD_COLOR):
    path = "./../upload/"
    img = imread(path + img_name, color_type)

    if img is None:
        raise FileNotFoundError(f"File Note Found: {path+img_name}")

    return img
