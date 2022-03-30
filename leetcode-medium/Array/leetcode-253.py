"""
https://leetcode.com/problems/meeting-rooms-ii/submissions/
99.71% Faster
"""
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        heappush(res, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= res[0]: heappop(res)
            heappush(res, interval[1])
        return len(res)


