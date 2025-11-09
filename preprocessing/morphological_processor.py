import cv2
import numpy as np


def auto_canny(img, k=1.0):
    sigma = img.std()  # Finding low/high contrast
    mean = img.mean()  # Finsing dark/bright image

    # thresholds from contrast
    lower = 0.66 * sigma
    upper = 1.33 * sigma

    # brightness compensation
    brightness_factor = np.clip(mean / 128, 0.5, 1.5)

    lower = int(max(0, lower * brightness_factor * k))
    upper = int(min(255, upper * brightness_factor * k))

    # img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.medianBlur(img, 3)
    return cv2.Canny(img, lower, upper), upper, lower


def morphologic_edge_detection(image):
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gradient)

    preprocessed = enhanced  # placeholder
    return preprocessed
