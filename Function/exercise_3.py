"""Exercise 3. Return Multiple Values from a Function

Practice Problem: Write a function calculation() that accepts two variables and calculates both addition and subtraction.
The function must return both results in a single return statement."""

def calculation(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return addition, subtraction

add,sub = calculation(30,30)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
