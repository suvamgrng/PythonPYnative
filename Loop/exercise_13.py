#   Count total number of digits in a number

digit = 75869
count = 0

while digit != 0:
    digit //= 10
    count += 1
print(f"Count: {count}")
