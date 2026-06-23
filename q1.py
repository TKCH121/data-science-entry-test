"""
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
"""

def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))): #Checks if x is a not a number - either integer or float, returning a -1 as failure signal 
        return -1
    else:
        x, y = y, x #python evaluates the right side then assigns them to the left
        print(f"x = {x}, y = {y}")

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
swap("Apple", 10) #will not print because Apple is neither an integer or a float
swap(9, 17) #will print x = 17 and y = 9
