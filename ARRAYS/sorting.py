# Given an array of integers nums, sort the array in non-decreasing order using the 
# selection sort algorithm and return the sorted array.


def selection_sort(nums):
    n=len(nums)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
nums = [5, 6, 4, 9]

print(selection_sort(nums))