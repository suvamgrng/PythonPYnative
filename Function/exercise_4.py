"""Exercise 4. Function with Default Argument

Practice Problem: Create a function show_employee() that accepts an employee’s name and salary.
If the salary is not provided in the function call, the function should automatically assign a default value of 9000."""

def show_employee(name, salary= 9000):
   return name, salary

employee_name, employee_salary = show_employee("Suvam Gurung", 12000)
print(f"Name: {employee_name}")
print(f"Salary: {employee_salary}")