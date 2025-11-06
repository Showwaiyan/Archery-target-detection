from cv2 import cvtColor, Laplacian, COLOR_BGR2GRAY, CV_64F


def detect_blur(image, threshold=100.0):
    grayscale_image = cvtColor(image, COLOR_BGR2GRAY)
    laplacian = Laplacian(grayscale_image, CV_64F)
    variance = laplacian.var()
    return variance < threshold, variance


def validate_brightness(image, light_threshold=90.0, dark_threshold=15.0):
    if len(image.shape) == 2:
        raise ValueError("Only grayscale image")
    mean_brightness = image.mean() * 100 / 255  # change to percentage

    if mean_brightness < dark_threshold:
        return -1  # -1 -> dark
    if mean_brightness > light_threshold:
        return 1  # 1 -> too bright

    return 0  # normal
