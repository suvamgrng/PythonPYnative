# Collatz Conjecture: Generate a sequence until it reaches 1

number = 6

while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = (number*3) + 1
    print(number, end=' ')
print()
