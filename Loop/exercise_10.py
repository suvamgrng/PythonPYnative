#   Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(list1), -1, -1):
    reversed_list.append(list1[i])
print(reversed_list)
