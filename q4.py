"""
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
"""

def string_reverse(s):
    if not isinstance(s, str):
        return -1
    return s[::-1]

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World"))
print(string_reverse("Python"))
