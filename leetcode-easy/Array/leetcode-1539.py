"""
Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.
Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
# Time and Space O(N). But, can you make it LogN? Will do that later
class Solution:
    def findKthPositive(self, arr, k):
        missing, res = {}, []
        for i in range(1, arr[-1]*10):
            if i not in missing: missing[i] = 1
            else: missing[i] += 1
        for i in arr: 
            if i in missing: missing[i] -= 1
        for i, j in missing.items():
            if j == 1: res.append(i)
        if len(res) == 1: return res[0]
        else: return res[k - 1]
        