#   Print the decreasing pattern

num = 5

for row in range(num, 0, -1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()
