# Reverse a integer number

num = 76542
reversed_number = 0

while 0 < num:
    # Get the last digit
    digit = num % 10
    # Add it to the reverse (shifting existing digits left)
    reversed_number = (reversed_number * 10) + digit
    # Remove the last digit from the original number
    num //= 10
print(f"Reversed number: {reversed_number}")
