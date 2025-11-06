import pytest
from unittest.mock import patch
import numpy as np
from cv2 import COLOR_RGB2BGR

from preprocessing.image_transformer import change_color_channel


def test_change_color_channel_valid():
    fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
    with patch("preprocessing.image_transformer.cvtColor") as mock_cvtColor:
        mock_cvtColor.return_value = "converted_image"

        result = change_color_channel(fake_img, COLOR_RGB2BGR)

        assert result == "converted_image"
        mock_cvtColor.assert_called_once_with(fake_img, COLOR_RGB2BGR)


def test_change_color_channel_invalid():
    fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
    invalid_channel = 99999  # some invalid value

    with pytest.raises(ValueError, match="unkown Color Channel"):
        change_color_channel(fake_img, invalid_channel)
