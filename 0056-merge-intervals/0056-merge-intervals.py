class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        result = []
        result.append(intervals[0])

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]

            last = result[-1]

            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                result.append([start, end])

        return result