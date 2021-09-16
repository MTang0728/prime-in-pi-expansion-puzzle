from sympy import N, pi
import numpy as np
import pytest

def generate_expan(expression, n):
    """
    a function that genererates an arbtrary large expansion of mathematical 
    expression based on user defined precision.
    input:
    - expression -> sympy expression
    - n -> int
    output:
    - my_expan -> sympy expression 
    """
    # generate expansion based on user-defined precision
    my_expan = N(expression, n)
    # return expanded excpression
    return my_expan

def check_prime(num):
    """
    a function that checks if user-entered number is a prime number.
    input:
    - num -> int
    output:
    - bool
    """
    # return False if num is less or equal to 1
    if num <= 1:
        return False
    else:
        # loop from 2 to the square root of the entered number
        # use as a divisor against the entered number
        for i in range(2, int(np.sqrt(num))+1):
            # check if the remainder is 0
            if num % i == 0:
                # return False
                return False
        # else it's True
        return True

def generate_window(number, length):
    """
    a function that generate sliding windows of user-defined length on a
    number.
    input:
    - number -> str
    - length -> int
    output:
    - windows -> list
    """
    # define an empty list for storing rolling window
    windows = []
    # get the total length of the number
    total_length = len(number)
    # loop through each element in the number
    for i in range(total_length - length + 1):
        # extract the number
        window = number[i:i+length]
        # append to the list
        windows.append(window)

    return windows


expansion_test_cases = [(pi, 10, 11),
                        (pi, 50, 51),
                        (17*pi, 30, 31),
                        ]
@pytest.mark.parametrize('expression, defined_length, expected_length', expansion_test_cases)
def test_expansion(expression, defined_length, expected_length):
    output_length = len(str(generate_expan(expression, defined_length)))

    assert output_length == expected_length


prime_test_cases = [(7, True),
                    (14159, True),
                    (14157, False),
                    (999983, True),
                    (0, False),
                    (-33, False)
                    ]
@pytest.mark.parametrize('tst_number, is_prime', prime_test_cases)
def test_prime(tst_number, is_prime):

    assert check_prime(tst_number) == is_prime


window_test_cases = [('123456789', 7, ['1234567', '2345678', '3456789']),
                    ('123456789', 9, ['123456789']),
                    ('12345', 1, ['1', '2', '3', '4', '5'])
                    ]
@pytest.mark.parametrize('string_number, window_size, output_windows', window_test_cases)
def test_prime(string_number, window_size, output_windows):
    generated_windows = generate_window(string_number, window_size)
    assert generated_windows == output_windows