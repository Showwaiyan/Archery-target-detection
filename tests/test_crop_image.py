import numpy as np
import pytest

from preprocessing.image_transformer import crop_image


def test_crop_image_valid():
    img = np.zeros((100, 200, 3), dtype=np.uint8)

    result = crop_image(img, x=10, y=20, w=50, h=40)

    assert result.shape == (40, 50, 3)


def test_crop_image_invalid_x():
    img = np.zeros((50, 50, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        crop_image(img, x=-1, y=10, w=10, h=10)

    with pytest.raises(ValueError):
        crop_image(img, x=100, y=10, w=10, h=10)


def test_crop_image_invalid_y():
    img = np.zeros((50, 50, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        crop_image(img, x=10, y=-5, w=10, h=10)

    with pytest.raises(ValueError):
        crop_image(img, x=10, y=100, w=10, h=10)
