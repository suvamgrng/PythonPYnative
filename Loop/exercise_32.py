#   List Rotation: Rotate elements left by k positions

nums = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
        first_letter = nums.pop(0)
        nums.append(first_letter)
print(nums)