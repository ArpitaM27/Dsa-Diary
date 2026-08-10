# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []

        for x in nums:
            heapq.heappush(heap, x)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]