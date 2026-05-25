"""Exercise 9. Print elements from a list present at odd index positions"""
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
print(result)