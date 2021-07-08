from strmath import *

def print_test():
    # Should return result 37.0
    test_a = "(9 + 10) * 6 / 3 - 4 % 3"
    print(test_a, '=', evaluate(test_a))

    # Should return result 17.7
    test_b = "13.2 + 4.5"
    print(test_b, '=', evaluate(test_b))

    # Should return result 0.03
    test_c = ".1 % .07"
    print(test_c, '=', evaluate(test_c))

    # Should return result 24.00
    test_d = "3. * (10.0 - 2)"
    print(test_d, '=', evaluate(test_d))