import pytest
from psd_tools import PSDImage
from zunda_psd.main import get_layer_path

@pytest.fixture()
def sample_layer() -> PSDImage:
    return PSDImage.open('sample.psd')


def test_layer_path(sample_layer):
    layer = sample_layer[4][1]
    path = '!口/*ほあ'

    assert path == get_layer_path(layer)
