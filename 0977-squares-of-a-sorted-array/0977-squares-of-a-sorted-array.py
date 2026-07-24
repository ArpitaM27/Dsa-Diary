class Solution(object):
    def sortedSquares(self, nums):
       arr=[]
       for x in nums:
           arr.append(x*x)
       arr=sorted(arr)
       return arr