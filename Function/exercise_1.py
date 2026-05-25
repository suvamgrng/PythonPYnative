"""Exercise 1. Create a Function with Parameters

Practice Problem: Write a function called demo() that accepts two parameters: a name and an age.
The function should print these values directly to the console."""

def demo(name, age):
    print("Name: ", name)
    print("Age: ", age)


user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

demo(user_name, user_age)