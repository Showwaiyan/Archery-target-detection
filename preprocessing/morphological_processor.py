import cv2
import numpy as np


def enhance_edges_for_detection(image):
    """
    Prepare an image for edge/circle detection using:
    - grayscale conversion
    - morphological gradient
    - contrast enhancement


    Args:
    image: Input BGR or grayscale image


    Returns:
    preprocessed: Image after gradient + contrast enhancement
    """
    # TODO: Convert to grayscale if needed
    # Example placeholder:
    if len(image.shape) != 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

    # TODO: Apply morphological gradient
    # Example placeholder:
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gradient)

    preprocessed = enhanced  # placeholder
    return preprocessed
