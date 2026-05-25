#   Check if a number is a palindrome

number = 192291
temp = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10

if temp == reversed_number:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
