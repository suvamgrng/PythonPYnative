"""Exercise 5. Create an Inner Function

Practice Problem: Create an outer function that accepts two parameters, a and b. Inside, create an inner function that
 calculates the addition of a and b.  The outer function should then add 5 to that sum and return the final result.
"""
def accept_values(a, b):
    # Inner function
    def calculate_values():
        return a + b
    
    # Call inner function and add 5 to the result
    add = calculate_values()
    return  add + 5

print(accept_values(2,3))