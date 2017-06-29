# test_mymath.py
import pytest
import mymath


def test_add_integers():
    """
    Test that the addition of two integers returns the correct total
    """
    result = mymath.add(1, 2)
    assert result == 3


def test_add_floats():
    """
    Test that the addition of two floats returns the correct result
    """
    result = mymath.add(10.5, 2)
    assert result == 12.5


def test_add_strings():
    """
    Test the addition of two strings returns the two string as one
    concatenated string
    """
    result = mymath.add('abc', 'def')
    assert result == 'abcdef'