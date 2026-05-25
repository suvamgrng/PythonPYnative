"""Exercise 4. Calculate the sum of all numbers from 1 to N"""
number = int(input("Enter a number: "))
total_sum = 0
for i in range(1, number+1):
    total_sum += i
print(f"Total sum of {number}: {total_sum}")
