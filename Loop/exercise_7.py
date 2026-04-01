#   Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    # Condition 3: Stop the loop if number > 500
    if i > 500:
        break
    
# Condition 2: Skip the number if > 150
    if i > 150:
        continue

    # Condition 1: Print if divisible by 5

    if i % 5 == 0:
        print(i)
