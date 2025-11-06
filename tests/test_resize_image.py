import pytest
from unittest.mock import patch
import numpy as np

from preprocessing.image_transformer import resize_image


def test_resize_image():
    with patch("preprocessing.image_transformer.resize") as mock_resize:
        fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
        mock_resize.return_value = fake_img

        fake_dimension = (100, 100)

        result = resize_image(fake_img, fake_dimension[0], fake_dimension[1])
        assert isinstance(result, np.ndarray)
        assert result.shape == (10, 10, 3)
        mock_resize.assert_called_once_with(
            mock_resize.call_args[0][0], mock_resize.call_args[0][1]
        )


def test_resize_image_with_invalid_dimension():
    with patch("preprocessing.image_transformer.resize") as mock_resize:
        fake_img = np.zeros((10, 10, 3), dtype=np.uint8)
        mock_resize.return_value = fake_img

        fake_dimension = (-10, 0)

        with pytest.raises(ValueError) as e_info:
            resize_image(fake_img, fake_dimension[0], fake_dimension[1])

        assert f"Invalid dimension: ({fake_dimension[0]}, {fake_dimension[1]})" in str(
            e_info.value
        )

        mock_resize.assert_not_called()
