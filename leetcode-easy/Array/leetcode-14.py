"""
https://leetcode.com/problems/longest-common-prefix/
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        # Time complexity is O(N) and space complexity is also O(N)
        """
        res = 'f'
        flow
        |
        flower, flow, flight
                      |
        temp = [o, o, i] --> 
        set(temp) = 2
        """
        # Edge case
        if strs == []: return str()
        res = ''
        min_length = len(min(strs))
        for i in range(min_length):
            temp = []
            for j in range(len(strs)): temp.append(strs[j][i])
            if len(set(temp)) == 1: res += temp[0]
            else: return res
        return res
            
            