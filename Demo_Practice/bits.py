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

# class Solution(object):
#     def hammingWeight(self, n):
#         count=0
#         while n:
#             n=n & (n-1)
#             count+=1
#         return count

# obj=Solution()
# n=2147483645
# print(obj.hammingWeight(n)) 


# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# class Solution(object):
#     def isPowerOfTwo(self, n):
#         if n <= 0:
#             return False

#         return (n & (n - 1)) == 0
    
# obj=Solution()
# n=0
# print(obj.isPowerOfTwo(n))

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
 
# class Solution(object):
#     def countBits(self, n):
#         arr=[0]* (n+1)
        
#         for i in range(0,n+1,1):
#             sum=0
#             j=i
#             while j:
#                 j=(j&(j-1))
#                 sum+=1
#             arr[i]=sum
#         return arr
         
         
# obj=Solution()
# n=2
# print(obj.countBits(n))

