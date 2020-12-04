# Test check whether or not a number is armstrong

# By definition Armstrong number is a number which is equal 
# to the sum of cube of its digit
def Armstrong(x):
    y = x
    total = 0
    while x > 0:
        a = x % 10
        total += int(a * a * a)
        x = int(x / 10)
    if y == total:
        return True
    else:
        return False


# Testing it for a fake Armstrong number
def test_method_1():
    assert Armstrong(343) == False


# Testing it for an Armstrong number
def test_method_2():
    assert Armstrong(153) == True
