# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        w_sum=0
        max_sum = float('-inf')
        for right in range(len(nums)):
            w_sum+=nums[right]
            if right-left+1==k:
                max_sum=max(max_sum,w_sum)
                w_sum -=nums[left]
                left+=1
        return max_sum/float(k)
    
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
class Solution(object):
    def twoSum(self, numbers, target):

     left=0
     right=len(numbers)-1
     
     while left<right:
      total=numbers[left]+numbers[right]
      if total==target:
          return [left+1,right+1]
      if total<target:
          left+=1
      if total>target:
          right-=1
    