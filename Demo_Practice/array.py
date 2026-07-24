# # Given an array nums, return true if the array was originally sorted in non-decreasing order, 
# # then rotated some number of positions (including zero). Otherwise, return false.

# # print("Enter the array elements separated by space:")
# # nums=list(map(int,input().split()))

# # count = 0

# # for i in range(len(nums)):
# #     if nums[i] > nums[(i + 1) % len(nums)]:
# #         count += 1

# # if count <= 1:
# #     print(True)
# # else:
# #     print(False)

# # Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# # You must write an algorithm with O(log n) runtime complexity.

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

# # Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# # You must write an algorithm with O(log n) runtime complexity

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

# # Given a binary array nums, return the maximum number of consecutive 1's in the array.

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
#         return max_count

# # Given a non-empty array of integers nums, every element appears twice except for one. Find that single one
# class Solution(object):
#     def singleNumber(self, nums):
#         result=0
#         for i in range(len(nums)):
#             result=result^nums[i]
#         return result 

# # Given an integer array nums, handle multiple queries of the following type:

# # Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# # Implement the NumArray class:

# # NumArray(int[] nums) Initializes the object with the integer array nums.
# # int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]). 

# class NumArray(object):

#     def __init__(self, nums):
        
#         self.prefix_sum = [0] * (len(nums))
#         self.prefix_sum[0] = nums[0]
#         for i in range(1, len(nums)):
#             self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]

    
#     def sumRange(self, left, right):
#         if left == 0:
#             return self.prefix_sum[right]
#         return self.prefix_sum[right] - self.prefix_sum[left - 1]
      
    
        
# # Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# # Return the running sum of nums.

# class Solution(object):
#     def runningSum(self, nums):
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         return nums


# # There is a biker going on a road trip. The road trip consists of n + 1 points at various altitudes. The biker starts his trip on point 0 with altitude equal 0.

# # You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

   
# class Solution(object):
#     def largestAltitude(self, gain):
#         max_altitude = 0
#         current_altitude = 0
#         for g in gain:
#             current_altitude += g
#             max_altitude = max(max_altitude, current_altitude)
#         return max_altitude

# # You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# # Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# # The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):

#         temp = nums1[:m]

#         for x in nums2:
#             temp.append(x)

#         temp.sort()

#         nums1[:] = temp[:]
       
        
# #  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# # Note that you must do this in-place without making a copy of the array.
       
       
# class Solution(object):
#     def moveZeroes(self, nums):
        
#            slow=[0]
#            for fast in range(len(nums)):
#                if nums[fast]!=0:
#                    nums[slow],nums[fast]=nums[fast],nums[slow]
#                    slow+=1
                  
               
#            return nums
                      
# # Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# # Specifically, ans is the concatenation of two nums arrays.

# # Return the array ans.

# class Solution(object):
#     def getConcatenation(self, nums):
      
#        return nums+nums
        
# # You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

# # You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

# # Return the array ans. Answers within 10-5 of the actual answer will be accepted.

# # Note that:

# # Kelvin = Celsius + 273.15
# # Fahrenheit = Celsius * 1.80 + 32.00 

# class Solution(object):
#     def convertTemperature(self, celsius):
       
#        k = celsius + 273.15
#        f = celsius * 1.80 + 32.00 
#        return [k,f]
       
# # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# # Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

# # The tests are generated such that there is exactly one solution. You may not use the same element twice.

# # Your solution must use only constant extra space.
# class Solution(object):
#     def twoSum(self, numbers, target):

#      left=0
#      right=len(numbers)-1
     
#      while left<right:
#       total=numbers[left]+numbers[right]
#       if total==target:
#           return [left+1,right+1]
#       if total<target:
#           left+=1
#       if total>target:
#           right-=1
    


# # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# # Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# # Return k.  

# class Solution(object):
#     def removeElement(self, nums, val):
#        fast=0
#        slow=0
#        while fast in range(len(nums)):
           
#            if nums[fast]!=val:
#                nums[slow]=nums[fast]
#                slow+=1
#            fast+=1
           
#        return slow
   
# # Given a string s consisting of words and spaces, return the length of the last word in the string.

# # A word is a maximal substring consisting of non-space characters only.  

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         s=s.split()
#         return len(s[-1])
    
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# class Solution(object):
#     def plusOne(self, digits):
#         x=int("".join(map(str,digits)))+1
        
#         arr=[]
#         for i in str(x):
#             arr.append(int(i))
#         return arr
# obj=Solution()
# digits=[1,8,9,5]
# res=obj.plusOne(digits)
# print(res)


