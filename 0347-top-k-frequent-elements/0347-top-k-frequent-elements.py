
class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        arr=[]
        for nums in nums:
            d[nums]=d.get(nums,0)+1
        for _ in range(k):
            x=max(d.values())
            for key in d:
                if d[key]==x:
                    arr.append(key)
                    del d[key]
                    break
        return arr
           