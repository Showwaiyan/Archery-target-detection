from cv2 import (
    resize,
    cvtColor,
    COLOR_RGB2BGR,
    COLOR_BGR2RGB,
    COLOR_BGR2GRAY,
    COLOR_RGB2GRAY,
)


def resize_image(image, new_width, new_height):
    if new_width <= 0 or new_height <= 0:
        raise ValueError(f"Invalid dimension: ({new_width}, {new_height})")

    resize_image = resize(image, (new_width, new_height))
    return resize_image


def change_color_channel(image, channel):
    if channel not in (COLOR_RGB2BGR, COLOR_BGR2RGB, COLOR_BGR2GRAY, COLOR_RGB2GRAY):
        raise ValueError(f"Can convert to unkown Color Channel: {channel}")

    result = cvtColor(image, channel)
    return result


def crop_image(image, x, y, w, h):
    image_height = len(image)
    image_width = len(image[0])

    if x < 0 or x > image_width:
        raise ValueError(f"Invalid Dimension to crop: x:{x}, y:{y}, w:{w}, h:{h}")

    if y < 0 or y > image_height:
        raise ValueError(f"Invalid Dimension to crop: x:{x}, y:{y}, w:{w}, h:{h}")

    result = image[y : y + h, x : x + w]
    return result
