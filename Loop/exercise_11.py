#   Reverse a string using a for loop (no slicing)
language = "Python"
reversed_string = []

for i in range(len(language)-1, -1, -1):
    reversed_string.append(language[i])
result = "".join(reversed_string)
print(result)
