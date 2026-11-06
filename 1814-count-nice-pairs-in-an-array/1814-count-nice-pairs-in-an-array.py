class Solution(object):
    def countNicePairs(self, nums):
        freq = {}
        count = 0
        MOD = 10**9 + 7

        for num in nums:
            rev_num = int(str(num)[::-1])
            key = num - rev_num

            count += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        return count % MOD