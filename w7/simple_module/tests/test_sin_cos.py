import math
import pytest
from trigonometry import sin, cos


@pytest.mark.parametrize('small_number', [0.001, 0.002, 0.0001, 0.003, 0.005])
def test_sin_small(small_number):
    assert round(sin(small_number), 4) == round(math.sin(small_number), 4)
    assert round(sin(-small_number), 4) == round(math.sin(-small_number), 4)


@pytest.mark.parametrize('small_number', [0.001, 0.002, 0.0001, 0.003, 0.005])
def test_cos_small(small_number):
    assert round(cos(small_number), 4) == round(math.cos(small_number), 4)
    assert round(cos(-small_number), 4) == round(math.cos(-small_number), 4)


@pytest.mark.xfail(reason='After update')
def test_failure():
    assert False

