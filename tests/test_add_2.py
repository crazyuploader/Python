# Simple test to check addition of two numbers


def Add_2(x, y):
    return x + y


def test_method_1():
    """
    Call Add_2() for integors
    """
    assert Add_2(5, 8) == 13


def test_method_2():
    """
    Call Add_2() for floating point
    """
    assert Add_2(5.2, 6.8) == 12
