#   Print full multiplication table (1 to 10)
num = 10

for i in range(1, num+1):
    for j in range(1, num + 1):
        print(f" {j}*{i} = {i*j}", end="\t")
    print()