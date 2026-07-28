class Solution(object):
    def maxArea(self, height):
     left=0
     right=len(height)-1
     
     best = 0
     while(left<right):
         base=right-left
         if height[right]==height[left]:
             area=base*height[left]
             right-=1
             best = max(best, area)
             continue
         if height[left]<height[right]:
             area=base*min(height[left],height[right])
             left=left+1
             best = max(best, area)
             continue
         if height[left]>height[right]:
             area=base*min(height[right],height[left])
             right=right-1
             best = max(best, area)
             continue
     return best
