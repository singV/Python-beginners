import pytest
import mymath


def test_subtract_integers():
    """
    Test that the addition of two integers returns the correct total
    """
    result = mymath.subtract(1, 2)
    assert result == -1


def test_subtract_floats():
    """
    Test that the addition of two floats returns the correct result
    """
    result = mymath.subtract(10.5, 2)
    assert result == 8.5
