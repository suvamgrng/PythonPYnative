#   Hollow square pattern

size = 5

for i in range(1, size):
    for j in range(1, size):
        if i == 1 or i == size or j == 1 or j == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
