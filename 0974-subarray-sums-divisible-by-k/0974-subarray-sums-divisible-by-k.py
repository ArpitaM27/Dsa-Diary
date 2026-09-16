class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix=0
        count=0
        seen={0:1}
        for x in nums:
            prefix+=x
            remainder=prefix%k
            if remainder in seen:
                
                count+=seen[remainder]
            
            seen[remainder] = seen.get(remainder, 0) + 1
        return count
                
        