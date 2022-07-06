"""
https://leetcode.com/problems/meeting-scheduler/
Given the availability time slots arrays slots1 and slots2 of two people and a meeting 
duration duration, return the earliest time slot that works for both of them and is of 
duration duration.
If there is no common time slot that satisfies the requirements, return an empty array.
The format of a time slot is an array of two elements [start, end] representing an 
inclusive time range from start to end.  
It is guaranteed that no two availability slots of the same person intersect with 
each other. That is, for any two time slots [start1, end1] and [start2, end2] of 
the same person, either start1 > end2 or start2 > end1.
Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []
"""

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        # Time Complexity is O(nLogN), Space is O(N)
        i, j = 0, 0
        sortedSlots1, sortedSlots2 = sorted(slots1), sorted(slots2)
        while i< len(sortedSlots1) and  j < len(sortedSlots2):
            start = max(sortedSlots1[i][0], sortedSlots2[j][0])
            end = min(sortedSlots1[i][1], sortedSlots2[j][1])
            diff = end-start
            if diff>=duration: return [start,start+duration]
            if sortedSlots2[j][1] - start < duration : j += 1
            if sortedSlots1[i][1] - start < duration : i += 1
        return []