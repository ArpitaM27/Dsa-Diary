    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=1
        k=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
                continue
                
            if nums[slow]!=nums[fast]:
                x=nums.pop(fast)
                nums.insert(slow+1,x)
                slow+=1
                fast+=1
                k+=1
                continue
        return k
        