"""
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
"""

def update_dictionary(dct, key, value):
    if key in dct: #checks if key already exist in dictionary
        print(f"Original value for key '{key}': {dct[key]}") #if key exists, print its current value before overwriting it
    dct[key] = value #if the key doesn't exist, it creates it, if it exists it overwrites it
    return dct

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print(update_dictionary({}, "name", "Alice")) #just adds new key
print(update_dictionary({"age": 25}, "age", 26)) #prints original value for key "age": 25, and then replaces key with "age": 26
