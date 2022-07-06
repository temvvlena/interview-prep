"""
https://leetcode.com/problems/merge-intervals/
Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        p = 0
        for i in range(1, len(intervals)):
            prev = intervals[p]
            cur = intervals[i]
            if prev[1]>=cur[0]:
                prev[0]=min(prev[0], cur[0])
                prev[1]=max(prev[1], cur[1])
            else: 
                p += 1
                intervals[p]=cur
        intervals = intervals[0:p + 1]
        return intervals
    """
    def merge-1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = res[len(res)-1]
            cur = intervals[i]
            if prev[1]>=cur[0]:
                prev[0]=min(prev[0], cur[0])
                prev[1]=max(prev[1], cur[1])
            else: res.append(cur)
        return res
    """