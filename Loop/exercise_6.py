#   Calculate the cube of all numbers from 1 to a given number

input_number = 6
cube = 1
for i in range(1, input_number+1):
    cube = i ** 3
    print(f"Current Number is {i} and the cube is {cube}")
