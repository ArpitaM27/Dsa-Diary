
class Solution(object):
    def sumOfUnique(self, nums):
        d={}
        res=0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            
        for x in d:
            
            if d[x]==1:
                res+=x
        return res
                