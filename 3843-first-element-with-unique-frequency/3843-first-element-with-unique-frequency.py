class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq={}
        double={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        c2 = Counter(freq.values())
        for x in nums:
               if c2[freq[x]]==1:
                   return x
        return -1
        
        