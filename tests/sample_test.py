import pytest

from pytemplate.sample import inc, is_prime


def test_inc():
    assert inc(4) == 5
    assert inc(-1) == 0


@pytest.mark.parametrize("x", [3, 37, 41, 11, 7, 97])
def test_is_prime(x):
    assert is_prime(x)


@pytest.mark.parametrize("x", [9, 18, 1000, 10, 1999990])
def test_is_not_prime(x):
    assert not is_prime(x)
