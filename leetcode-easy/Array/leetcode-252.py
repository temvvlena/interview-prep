"""
https://leetcode.com/problems/meeting-rooms/
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            elif merged[-1][-1] > interval[0]:
                return False
            else:
                merged.append(interval)
        return True