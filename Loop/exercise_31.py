#    Even/Odd Segregation: Move evens to front, odds to back

original = [1, 2, 3, 4, 5, 6]
segregated_list = []
odd = []
even = []
for num in original:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
segregated_list = even + odd
print(f"Segregated List: {segregated_list}")
