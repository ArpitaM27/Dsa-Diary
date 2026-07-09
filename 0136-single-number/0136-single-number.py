class Solution(object):
    def singleNumber(self, nums):
        result=0
        for i in range(len(nums)):
            result=result^nums[i]
        return result