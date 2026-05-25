"""Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1"""
number = int(input("Enter a number: "))

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3*number + 1
    print(number, end = ", ")