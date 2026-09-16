class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        seen={0:1}
        for x in nums:
            prefix+=x
            if prefix-k in seen:
               count+=seen[prefix-k]
            seen[prefix] = seen.get(prefix, 0) + 1
        return count

        