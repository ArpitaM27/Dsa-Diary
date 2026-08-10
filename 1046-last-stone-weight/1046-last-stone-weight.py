import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []

        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            if a != b:
                heapq.heappush(heap, -(a - b))

        if heap:
            return -heap[0]

        return 0
       