class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        if k % 2 == 1:
            smallest = min(range(len(nums)), key=lambda i: abs(nums[i]))
            nums[smallest] = -nums[smallest]

        return sum(nums)