import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x*x + y*y

            heapq.heappush(heap, (-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for distance, point in heap]