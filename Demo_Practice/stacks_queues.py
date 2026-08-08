# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# class Solution(object):
#     def isValid(self, s):

#         stack = []

#         pairs = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         for ch in s:

#             if ch in "([{":
#                 stack.append(ch)

#             else:
#                 if not stack:
#                     return False

#                 if stack[-1] != pairs[ch]:
#                     return False

#                 stack.pop()

#         return len(stack) == 0

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 
# class Solution(object):
#     def removeDuplicates(self, s):
#         stack=[]
#         for ch in s:
        
#             if stack and stack[-1]==ch:
#                 stack.pop()
                
#             else:
#                 stack.append(ch)
                
#         return "".join(stack)
# obj=Solution()
# s = "abbaca"
# print(obj.removeDuplicates(s))

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.  


# class Solution(object):
#     def calPoints(self, operations):
#         stack=[]
#         for x in operations:
#             if stack and x=="C":
#                 stack.pop()
#                 continue
#             if stack and x=="D":
#                 y=stack[-1]
#                 stack.append(2*y)
#                 continue
#             if stack and x=="+":
#                 y=int(stack[-2])
#                 z=int(stack[-1])
#                 k=y+z
#                 stack.append(k)
#                 continue
#             else:
#                 stack.append(int(x))
#                 continue
       
#         return sum(stack)
# obj=Solution()
# ops = ["1","C"]
# print(obj.calPoints(ops))

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above      


# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         d={}
#         stack=[]
#         for num in nums2:
#             while stack and num>stack[-1]:
#                  d[stack.pop()] = num
#             stack.append(num)

#         while stack:
#             d[stack.pop()] = -1

#         return [d[num] for num in nums1]
    
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means
# you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means
# you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# class Solution(object):
#     def nextGreaterElements(self, nums):
    
#        arr = [-1] * len(nums)
#        stack=[]
#        i=0
#        for i in range(2*len(nums)):
#            idx=i%len(nums)
#            while stack and nums[idx]>nums[stack[-1]]:
#                arr[stack.pop()]=(nums[idx])
#            if i<len(nums):
#             stack.append(idx)
      
#        return arr

#     Given an array of integers temperatures represents the daily temperatures, return an
#     array answer such that answer[i] is the number of days you have to wait after the ith day to get 
#     a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#       arr=[0]*len(temperatures)
#       stack=[]
#       i=0
#       for i in range(len(temperatures)):
#           while stack and temperatures[i]>temperatures[stack[-1]]:
#               distance=i-(stack[-1])
#               arr[stack.pop()]=distance
#           stack.append(i)
#       return arr                            


