"""Exercise 6. Calculate the cube of all numbers from 1 to a given number"""
number = int(input("Enter a number: "))
cube = 1
for i in range(1,number+1):
    cube = i**3
    print(cube, end=" ")