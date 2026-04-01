#   Count occurrences of a specific element in a list

list1 = [10, 20, 10, 30, 10, 40, 50]
count = 0
target = 10

for i in list1:
    if i == target:
        count += 1
print(f"{target} appears {count} times")
