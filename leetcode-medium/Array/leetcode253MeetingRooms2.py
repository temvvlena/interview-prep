"""
https://leetcode.com/problems/meeting-rooms-ii/
Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1: return 1
        s_int = sorted(intervals, key=lambda x: x[0])
        e_int = sorted(intervals, key=lambda x: x[1])
        count = 1
        n = 0
        for i in range(1, len(s_int)): 
            if s_int[i][0] < e_int[n][1]: count += 1
            else: n += 1
        return count