#   Armstrong Number Check

num = 153
num_str = str(num)
power = len(num_str)
total = 0

for i in num_str:
    total += int(i) ** power

if total == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")
