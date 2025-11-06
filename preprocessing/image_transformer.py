from cv2 import resize


def resize_image(image, new_width, new_height):
    if new_width <= 0 or new_height <= 0:
        raise ValueError(f"Invalid dimension: ({new_width}, {new_height})")

    resize_image = resize(image, (new_width, new_height))
    return resize_image
