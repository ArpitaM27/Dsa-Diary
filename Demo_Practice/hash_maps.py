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
            if x in d1:
                d1[x]+=1
            else:
                d1[x]=1
        for y in s:
            if y in d2:
                d2[y]+=1
            else:
                d2[y]=1
        return d1==d2