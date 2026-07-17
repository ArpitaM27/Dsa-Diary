class Solution(object):
    def merge(self, nums1, m, nums2, n):

        temp = nums1[:m]

        for x in nums2:
            temp.append(x)

        temp.sort()

        nums1[:] = temp[:]
       
        