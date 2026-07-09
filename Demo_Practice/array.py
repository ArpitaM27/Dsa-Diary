# Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# then rotated some number of positions (including zero). Otherwise, return false.

# print("Enter the array elements separated by space:")
# nums=list(map(int,input().split()))

# count = 0

# for i in range(len(nums)):
#     if nums[i] > nums[(i + 1) % len(nums)]:
#         count += 1

# if count <= 1:
#     print(True)
# else:
#     print(False)

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# class Solution:
#     def searchInsert(self, nums, target):
#         low=0
#         high=len(nums)-1
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return low

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity

# class Solution(object):
#     def search(self,nums,target):
#         low=0
#         high=len(nums)-1
#         while low<=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return -1

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         max_count=0
#         current_count=0
#         for i in range(len(nums)):
#             if nums[i]==1:
#                 current_count+=1
#                 max_count=max(max_count,current_count)
#             else:
#                 current_count=0
#         return max_counts

