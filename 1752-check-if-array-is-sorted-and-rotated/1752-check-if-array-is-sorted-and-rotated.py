# class Solution:
#     def check(self, nums):
#         count = 0

#         for i in range(len(nums)):
#             if nums[i] > nums[(i + 1) % len(nums)]:
#                 count += 1

#         if count <= 1:
#             return True
#         else:
#             return False
        
class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum