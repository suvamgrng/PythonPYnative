"""Exercise 2. Variable Length of Arguments (*args)

Practice Problem: Create a function func1() such that it can accept a variable number of arguments and print all of them.
Whether you pass two numbers or five, the function should handle them all without error."""

def  func1(*args):
    print("Printing values:")
    for i in range(len(args)):  # Haha wanted to try some range() function🤣
        print(args[i])

func1(12,12,29)
func1(12,23)
