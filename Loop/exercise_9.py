#   Print elements from a list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_list = []
for i, val in enumerate(my_list):
    if i % 2 != 0:
        odd_list.append(val)
print(odd_list)
