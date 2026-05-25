"""Remove duplicates without set"""

dup_list = [1, 2, 2, 3, 4, 4, 4, 5]

unique_list = []

for num in dup_list:
    if num not in unique_list:
        unique_list.append(num)

print(f"Unique List: {unique_list}")
