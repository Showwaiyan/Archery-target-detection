# Function to load an image from file path
# Function to display image in a window
from cv2 import (
    imread,
    imshow,
    namedWindow,
    waitkey,
    destroyAllWindows,
    IMREAD_COLOR,
    WINDOW_AUTOSIZE,
)


def load_image(img_name, color_type=IMREAD_COLOR):
    path = "./../upload/"
    img = imread(path + img_name, color_type)

    if img is None:
        raise FileNotFoundError(f"File Note Found: {path+img_name}")

    return img


def show_image(image, name, size=WINDOW_AUTOSIZE):
    if image is None:
        raise ValueError("Invalid Image: image value is None")

    namedWindow(name, size)
    imshow(name, image)
    waitkey(0)
    destroyAllWindows()
