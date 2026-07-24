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
 

# class Solution(object):
#     def rotateString(self, s, goal):
#         if len(s) !=len(goal):
#             return False
#         if s in goal+goal:
#             return True
#         return False
        
#     # Write a function that reverses a string. The input string is given as an array of characters s.

# # You must do this by modifying the input array in-place with O(1) extra memory.

 

# class Solution(object):
#     def reverseString(self, s):
#         slow=0
#         fast=len(s)-1
#         while slow<fast:
#             s[slow],s[fast]=s[fast],s[slow]
#             slow+=1
#             fast-=1
#         return s

# # Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# # A string is represented by an array if the array elements concatenated in order forms the string.
# class Solution(object):
#     def arrayStringsAreEqual(self, word1, word2):
#         arr="".join(word1)
#         arr1="".join(word2)
#         if arr==arr1:
#             return True
#         else:
#             return False
        
# # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# # Given a string s, return true if it is a palindrome, or false otherwise.

# class Solution(object):
#  def isPalindrome(self, s):
#   s=s.lower()     
#   left = 0
#   right = len(s) - 1
#   while left < right:

#     if not s[left].isalnum():
#         left += 1
#         continue

#     if not s[right].isalnum():
#         right -= 1
#         continue

#     if s[left] != s[right]:
#         return False

#     left += 1
#     right -= 1

#   return True

# # Given an input string s, reverse the order of the words.

# # A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# # Return a string of the words in reverse order concatenated by a single space.

# # Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# class Solution(object):
#     def reverseWords(self, s):
#           s=s.split()
#           slow=0
#           fast=len(s)-1
#           while slow<fast:
#             s[slow],s[fast]=s[fast],s[slow]
#             slow+=1
#             fast-=1
#           s=" ".join(s)
#           return s

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1  

# from math import factorial
# class Solution(object):
#     def trailingZeroes(self, n):
#         x=factorial(n)
#         count=0
#         x=str(x)
#         i=len(x)-1
#         while x[i]=='0':
#             count+=1
#             i=i-1
            
    
#         return count
    
# obj=Solution()
# n=10
# print(obj.trailingZeroes(n))