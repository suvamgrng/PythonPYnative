#   Find largest and smallest digit in a number

num = 97586

digit = [int(d) for d in str(num)]

minimum = digit[0]
maximum = digit[0]

for i in digit:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print(f"Minimum: {minimum}")
print(f"Max: {maximum}")
