import pytest


@pytest.mark.parametrize('a', [1, 3, 5])
def test_something(a):
    assert a % 2 == 1

