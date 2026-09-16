class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix=0
        count=0
        seen={0:1}
       
        for x in nums:
            prefix+=x
            need=prefix-goal
            if need in seen:
                count+=seen[need]
            seen[prefix] = seen.get(prefix, 0) + 1
        return count
            
