"""Exercise 16. Check if a number is a palindrome"""
number = 121
original_number = number
reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10
is_palindrome = reversed_number == original_number

if is_palindrome:
    print("Yes it is palindrome")
else:
    print("Nope bro, its not a palindrome")