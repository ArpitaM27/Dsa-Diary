class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        w_sum=0
        max_sum = float('-inf')
        for right in range(len(nums)):
            w_sum+=nums[right]
            if right-left+1==k:
                max_sum=max(max_sum,w_sum)
                w_sum -=nums[left]
                left+=1
        return max_sum/float(k)
        