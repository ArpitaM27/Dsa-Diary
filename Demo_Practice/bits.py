# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# class Solution(object):
#     def singleNumber(self, nums):
#         result=0
#         for i in range(len(nums)):
#             result=result^nums[i]
#         return result

#  Given a positive integer n, write a 
#  function that returns the number of set bits in its binary representation (also known as the Hamming weight).

class Solution(object):
    def hammingWeight(self, n):
        count=0
        while n:
            n=n & (n-1)
            count+=1
        return count

obj=Solution()
n=2147483645
print(obj.hammingWeight(n))