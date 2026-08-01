class Solution(object):
    def removeDuplicates(self, nums):
      slow=2
      
      for fast in range(2,len(nums)):
           if nums[fast]!=nums[slow-2]:
               nums[slow]=nums[fast]
               slow+=1
      return slow
            