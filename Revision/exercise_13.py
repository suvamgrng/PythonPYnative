"""Exercise 13. Count total number of digits in a number"""
number = 1234567
count = 0

while number != 0:
    number //= 10
    count += 1
print(f"Total digits count: {count}")