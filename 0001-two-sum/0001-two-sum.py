class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
                need=target-nums[i]
                if need in d:
                  return[i,d[need]]
                d[nums[i]]=i
        return False