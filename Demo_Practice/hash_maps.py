# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 

class Solution(object):
    def containsDuplicate(self, nums):
       d={}
       for x in nums:
           if x in d:
               return True
           else:
               d[x]=1
       return False
   
#using sets
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for x in nums:
            if x in seen:
                return True

            seen.add(x)

        return False

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        d1={}
        d2={}
        for x in t:
                d1[x]=d1.get(x,0)+1
        for y in s:
                d2[x]=d2.get(y,0)+1
                
        return d1==d2
    
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
 
class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
    
        for i in range(len(s)):
            if d[s[i]]==1:
              return i
        return -1
           

