"""
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
"""

def string_reverse(s):
    if not isinstance(s, str): #checks if "s" is a string, returns -1 if not
        return -1
    return s[::-1] #slicing operation to look at the entire string, and walk backwards through it

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

print(string_reverse("Hello World")) #dlroW olleH
print(string_reverse("Python")) #nohtyP
