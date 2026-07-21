
class Solution(object):
    def removeElement(self, nums, val):
       fast=0
       slow=0
       while fast in range(len(nums)):
           
           if nums[fast]!=val:
               nums[slow]=nums[fast]
               slow+=1
           fast+=1
           
       return slow