import numpy as np
import pytest

from preprocessing.image_validator import validate_contrast


def test_validate_contrast_non_grayscale():
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        validate_contrast(img)


def test_validate_contrast_low():
    img = np.full((100, 100), 50, dtype=np.uint8)  # almost no variation

    result = validate_contrast(img)
    assert result == -1


def test_validate_contrast_high():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[::2] = 255  # alternating rows → strong contrast

    result = validate_contrast(img)
    assert result == 1


def test_validate_contrast_normal():
    img = np.tile(np.arange(100), (100, 1)).astype(np.uint8)  # smooth gradient

    result = validate_contrast(img)
    assert result == 0
