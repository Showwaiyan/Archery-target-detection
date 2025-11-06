import pytest
from unittest.mock import patch
import numpy as np
from cv2 import COLOR_RGB2BGR

from preprocessing.image_loader import load_image, change_color_channel


def test_load_image_that_exist():
    with patch("preprocessing.image_loader.imread") as mock_imread:
        fake_img = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_imread.return_value = fake_img

        result = load_image("cat.jpg")

        assert (result == fake_img).all()
        assert isinstance(result, np.ndarray)
        assert result.shape == (100, 100, 3)
        mock_imread.assert_called_once_with(
            "./../upload/cat.jpg", mock_imread.call_args[0][1]
        )


def test_load_image_that_not_exist():
    with patch("preprocessing.image_loader.imread") as mock_imread:
        fake_img = None
        mock_imread.return_value = fake_img

        with pytest.raises(FileNotFoundError) as e_info:
            load_image("cat.jpg")

        assert "cat.jpg" in str(e_info.value)
        mock_imread.assert_called_once_with(
            "./../upload/cat.jpg", mock_imread.call_args[0][1]
        )


def test_load_image_with_other_color():
    with patch("preprocessing.image_loader.imread") as mock_imread:
        fake_img = np.zeros((100, 100, 3), dtype=np.uint8)
        mock_imread.return_value = fake_img

        custom_flag = 0
        result = load_image("cat.jpg", custom_flag)

        assert isinstance(result, np.ndarray)
        mock_imread.assert_called_once_with("./../upload/cat.jpg", custom_flag)


def test_change_color_channel_valid():
    fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
    with patch("preprocessing.image_loader.cvtColor") as mock_cvtColor:
        mock_cvtColor.return_value = "converted_image"

        result = change_color_channel(fake_img, COLOR_RGB2BGR)

        assert result == "converted_image"
        mock_cvtColor.assert_called_once_with(fake_img, COLOR_RGB2BGR)


def test_change_color_channel_invalid():
    fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
    invalid_channel = 99999  # some invalid value

    with pytest.raises(ValueError, match="unkown Color Channel"):
        change_color_channel(fake_img, invalid_channel)
