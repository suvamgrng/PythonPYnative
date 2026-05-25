"""Exercise 15. Find largest and smallest digit in a number"""
number = 75869

digit = [int(char) for char in str(number)]

max_num = digit[0]
min_num = digit[0]

for item in digit:
    if item > max_num:
        max_num = item

    if item < min_num:
        min_num = item
print(f"Largest number: {max_num}")
print(f"Smallest number: {min_num}")
