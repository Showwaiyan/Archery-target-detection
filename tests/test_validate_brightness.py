import numpy as np
import pytest

from preprocessing.image_validator import validate_brightness


def test_validate_brightness_grayscale():
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        validate_brightness(img)


def test_validate_brightness_dark():
    img = np.full((100, 100), 5, dtype=np.uint8)  # very dark

    result = validate_brightness(img)
    assert result == -1


def test_validate_brightness_bright():
    img = np.full((100, 100), 250, dtype=np.uint8)  # almost white

    result = validate_brightness(img)
    assert result == 1


def test_validate_brightness_normal():
    img = np.full((100, 100), 120, dtype=np.uint8)  # mid brightness

    result = validate_brightness(img)
    assert result == 0
