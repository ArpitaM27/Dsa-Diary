
class Solution(object):
    def sortArrayByParity(self, nums):
       slow=0
       fast=0
       while fast<len(nums):
           if nums[fast]%2==0:
               nums[slow],nums[fast]=nums[fast],nums[slow]
               slow+=1
           fast+=1
       return nums