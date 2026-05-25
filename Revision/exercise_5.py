"""Exercise 4. Print multiplication table of a given number"""
number = int(input("Enter a number: "))
result = [str(number*i) for i in range(1, 10+1)]
print(result)