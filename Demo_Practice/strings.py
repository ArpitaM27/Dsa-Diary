# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".



# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return ""
#         shortest = min(strs, key=len)
#         for i in range(len(shortest)):
#             for string in strs:
#                 if string[i] != shortest[i]:
#                     if i == 0:
#                         return ""
#                     return shortest[:i]

#         return shortest  

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

class Solution(object):
    def rotateString(self, s, goal):
        if len(s) !=len(goal):
            return False
        if s in goal+goal:
            return True
        return False
        