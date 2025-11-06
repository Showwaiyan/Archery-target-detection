from cv2 import cvtColor, Laplacian, COLOR_BGR2GRAY, CV_64F


def validate_blur(image, threshold=100.0):
    grayscale_image = cvtColor(image, COLOR_BGR2GRAY)
    laplacian = Laplacian(grayscale_image, CV_64F)
    variance = laplacian.var()
    return variance < threshold, variance


def validate_brightness(image, light_threshold=90.0, dark_threshold=15.0):
    if len(image.shape) != 2:
        raise ValueError("Only grayscale image is acceptable")
    mean_brightness = image.mean() * 100 / 255  # change to percentage

    if mean_brightness < dark_threshold:
        return -1  # -1 -> dark
    if mean_brightness > light_threshold:
        return 1  # 1 -> too bright

    return 0  # normal


def validate_contrast(image, low_threshold=20.0, high_threshold=80):
    if len(image.shape) != 2:
        raise ValueError("Only grayscale image is acceptable")
    contrast = image.std()

    if contrast < low_threshold:
        return -1  # -1 -> low
    if contrast > high_threshold:
        return 1  # 1 -> high

    return 0  # normal
