# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Two intervals are considered overlapping if they share at least one point.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.    


# class Solution(object):
#     def insert(self, intervals, newInterval):
#         result = []

#         for interval in intervals:

#             if interval[1] < newInterval[0]:
#                 result.append(interval)

#             elif interval[0] > newInterval[1]:
#                 result.append(newInterval)
#                 newInterval = interval

#             else:
#                 newInterval[0] = min(newInterval[0], interval[0])
#                 newInterval[1] = max(newInterval[1], interval[1])

#         result.append(newInterval)

#         return result


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# class Solution(object):
#     def merge(self, intervals):
#         intervals.sort()

#         result = []
#         result.append(intervals[0])

#         for interval in intervals[1:]:
#             start = interval[0]
#             end = interval[1]

#             last = result[-1]

#             if start <= last[1]:
#                 last[1] = max(last[1], end)
#             else:
#                 result.append([start, end])

#         return result


# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b


class Solution(object):
    def summaryRanges(self, nums):
        arr = []
        
        if not nums:
            return arr

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    arr.append(str(start))
                else:
                    arr.append(str(start) + "->" + str(nums[i-1]))

                start = nums[i]

        if start == nums[-1]:
            arr.append(str(start))
        else:
            arr.append(str(start) + "->" + str(nums[-1]))

        return arr