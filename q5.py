"""
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
"""

def check_divisibility(num, divisor):
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))): #check that both values is either an integer or a float, return -1 if not
        return -1
    return num % divisor == 0 #modulo operator to return the remainder - remainder = 0 means the number is perfectly divisible without remainders


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2)) #True
print(check_divisibility(7, 3)) #False
