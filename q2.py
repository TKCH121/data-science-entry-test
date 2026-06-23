"""
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
"""

def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list): #check that lst is a list, returns -1 if not
        return -1
    lst = [replace_val if item == find_val else item for item in lst] #Loops through every value in lst and builds a new modifed lst where if a value is equal to item, it gets replaced by replace_val, otherwise it keeps the original item
    return lst #returns modified list

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)) #replaces 3 instances of "2" with "5" to return [1, 5, 3, 4, 5, 5]
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange")) #replaces 2 instances of "apple" with "orange" to return ["orange","banana", "orange"]
