
class Solution(object):
    def nextGreaterElements(self, nums):
    
       arr = [-1] * len(nums)
       stack=[]
       i=0
       for i in range(2*len(nums)):
           idx=i%len(nums)
           while stack and nums[idx]>nums[stack[-1]]:
               arr[stack.pop()]=(nums[idx])
           if i<len(nums):
            stack.append(idx)
      
       return arr
    