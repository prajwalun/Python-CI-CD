import pytest
from math_utils import MathUtils


# Test methods
@pytest.fixture
def math_utils_obj():
    return MathUtils()


def test_add(math_utils_obj):
    assert math_utils_obj.add(4, 4) == 8
    assert math_utils_obj.add(-1, 2) == 1
    assert math_utils_obj.add(0, 0) == 0


def test_subtract(math_utils_obj):
    assert math_utils_obj.subtract(5, 3) == 2
    assert math_utils_obj.subtract(2, 5) == -3
    assert math_utils_obj.subtract(0, 0) == 0


def test_multiply(math_utils_obj):
    assert math_utils_obj.multiply(4, 2) == 8
    assert math_utils_obj.multiply(-3, 3) == -9
    assert math_utils_obj.multiply(0, 5) == 0


def test_divide(math_utils_obj):
    assert math_utils_obj.divide(6, 3) == 2.0
    assert math_utils_obj.divide(-6, 3) == -2.0
    assert math_utils_obj.divide(15, 5) == 3.0
    assert math_utils_obj.divide(9, 0) == -1.0
