class Solution(object):
    def intersection(self, nums1, nums2):
        s = set(nums1)
        result = []

        for x in nums2:
            if x in s:
                result.append(x)
                s.remove(x)

        return result