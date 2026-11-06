class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        d={}
        for a in nums1:
            for b in nums2:
                total=a+b
                d[total]=d.get(total,0)+1
        count=0
        for c in nums3:
            for f in nums4:
                total=c+f
                count+=d.get(-total,0)
        return count