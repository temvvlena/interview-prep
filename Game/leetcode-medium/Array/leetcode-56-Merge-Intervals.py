"""
https://leetcode.com/problems/merge-intervals/
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [1,3],[2,6],[8,10],[15,18]
        [1,6],[8,10],[15,18]
        [1,3],[2,6],[8,10],[15,18]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        output = []

        for interval in intervals:
            if len(output) == 0 or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output

