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