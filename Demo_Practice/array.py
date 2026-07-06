# Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of positions (including zero). Otherwise, return false.

print("Enter the array elements separated by space:")
nums=list(map(int,input().split()))

count = 0

for i in range(len(nums)):
    if nums[i] > nums[(i + 1) % len(nums)]:
        count += 1

if count <= 1:
    print(True)
else:
    print(False)