import pytest
from unittest.mock import patch
import numpy as np

from preprocessing.image_loader import load_image


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
