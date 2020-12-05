# Test for checking average of number(s)

def Average(x):
    total = 0
    for number in x:
        total = total + number
    return total / len(x)


def test_method_1():
    numbers = [1, 2, 3]
    assert Average(numbers) == 2


def test_method_2():
    numbers = [3.7, 2.3, 5.9, 7.4]
    assert Average(numbers) == 4.825