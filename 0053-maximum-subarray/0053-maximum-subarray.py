class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        current = nums[0]
        answer = nums[0]

        for x in nums[1:]:

            current = max(x, current + x)

            answer = max(answer, current)

        return answer

        
        