# Test for base_exponent_power.py program


def Base_Exponent_Power(x, y):
    result = 1
    while y != 0:
        result *= x
        y -= 1
    return result


def test_method_1():
    assert Base_Exponent_Power(2, 3) == 8


def test_method_2():
    assert Base_Exponent_Power(3, 3) == 27
