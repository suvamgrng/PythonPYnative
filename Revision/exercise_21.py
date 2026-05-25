"""
Exercise 8. Count occurrences of a specific element in a list
"""
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for item in list1:
    if target==item:
        count += 1

print(f"The target {target} appeared: {count}")
