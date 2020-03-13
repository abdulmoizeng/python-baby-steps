def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def wrong_subtraction(a, b):
    return a - b - 1


def wrong_addition(a, b):
    return a + 1 + b


def test_addition():
    assert addition(3, 3) == 6
    print("Test Passed")


def test_subtraction():
    assert subtraction(7, 6) == 1
    print("Test 2 Passed")


def test_wrong_addition():
    assert wrong_addition(100, 100) == 200
    print("This will not be printed")
    # AssertionError would be printed out


def test_wrong_subtraction():
    assert wrong_subtraction(101, 100) == 1
    print("This will not be printed")
    # AssertionError would be printed out


if __name__ == '__main__':
    test_addition()
    test_subtraction()
    test_wrong_addition()
    test_wrong_subtraction()
