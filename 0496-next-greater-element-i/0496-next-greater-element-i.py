class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        d={}
        stack=[]
        for num in nums2:
            while stack and num>stack[-1]:
                 d[stack.pop()] = num
            stack.append(num)

        while stack:
            d[stack.pop()] = -1

        return [d[num] for num in nums1]