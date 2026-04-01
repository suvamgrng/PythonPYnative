#   Calculate the sum of all numbers from 1 to N

number = int(input("Enter number: "))
sum = 0

for i in range(1, number+1):
    sum += i
print(f"Sum is {sum}")
