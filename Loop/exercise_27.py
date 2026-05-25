#    List Cumulative Sum: Each element is the sum of all previous

list_num = [1, 2, 3, 4]
cumulative_sum = []
current_sum = 0

for i in range(len(list_num)):
    current_sum += list_num[i]
    cumulative_sum.append(current_sum)

print(f"Cumulative sum: {cumulative_sum}")