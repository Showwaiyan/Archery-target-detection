# Function to load an image from file path
# Function to display image in a window
from cv2 import (
    imread,
    imshow,
    namedWindow,
    waitKey,
    destroyAllWindows,
    cvtColor,
    IMREAD_COLOR,
    WINDOW_AUTOSIZE,
    COLOR_RGB2BGR,
    COLOR_BGR2RGB,
    COLOR_BGR2GRAY,
    COLOR_RGB2GRAY,
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
    waitKey(0)
    destroyAllWindows()


def change_color_channel(image, channel):
    if channel not in (COLOR_RGB2BGR, COLOR_BGR2RGB, COLOR_BGR2GRAY, COLOR_RGB2GRAY):
        raise ValueError(f"Can convert to unkown Color Channel: {channel}")

    result = cvtColor(image, channel)
    return result
