# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 
# import heapq

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         heap = []

#         for x in nums:
#             heapq.heappush(heap, x)

#             if len(heap) > k:
#                 heapq.heappop(heap)

#         return heap[0]
    
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[]
        for x in stones:
            heapq.heappush(heap,-x)
        while len(heap) > 1:
                a=-heapq.heappop(heap)
                b=-heapq.heappop(heap)
                if a != b:
                 heapq.heappush(heap, -(a-b))
        if heap:
            return -heap[0]

        return 0