"""
https://leetcode.com/problems/excel-sheet-column-number/
Excel Sheet Column Number
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1:
Input: columnTitle = "A"
Output: 1
Example 2:
Input: columnTitle = "AB"
Output: 28
Example 3:
Input: columnTitle = "ZY"
Output: 701
Example 4:
Input: columnTitle = "FXSHRXW"
Output: 2147483647
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        aHash = {}
        ans = 0
        val = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(val)): aHash[val[i]] = i+1
        # Case 1 Z
        if len(columnTitle) == 1: return aHash[columnTitle]
        for i in range(len(columnTitle)):
            temp = columnTitle[len(columnTitle)-1-i]
            ans += (aHash[temp]*(26**i))
        return ans
        