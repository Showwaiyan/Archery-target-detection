import cv2
import numpy as np
from preprocessing.image_validator import detect_blur


def test_detect_blur_sharp_image():
    # create synthetic sharp image (white square on black)
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), (255, 255, 255), -1)
    is_blur, score = detect_blur(img, threshold=100.0)
    assert not is_blur
    assert score > 100.0


def test_detect_blur_blurred_image():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), (255, 255, 255), -1)
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    is_blur, score = detect_blur(blurred, threshold=100.0)
    assert is_blur
    assert score < 100.0
