#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using recursion.
    
    Parameters:
    n (int): The non-negative integer to compute the factorial for.
    
    Returns:
    int: The factorial value of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
