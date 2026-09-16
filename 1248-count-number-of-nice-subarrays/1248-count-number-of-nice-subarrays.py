class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        seen={0:1}
        for i,x in enumerate(nums):
            if x%2==1:
                prefix+=1
            
            if prefix-k in seen:
                count+=seen[prefix-k]
            seen[prefix]=seen.get(prefix,0)+1
        return count
        