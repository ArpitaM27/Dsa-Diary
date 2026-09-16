class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix=0
        seen={0:-1}
        length=0
        for i,x in enumerate(nums):
            if x==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in seen:
                length=max(length,i-seen[prefix])
            else:
                    seen[prefix]=i
        return length
                

            
        
        