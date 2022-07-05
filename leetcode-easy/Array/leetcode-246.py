"""
https://leetcode.com/problems/strobogrammatic-number/
246. Strobogrammatic Number
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        myHash = {"6": "9", "8": "8", "1": "1", "0": "0", "9": "6"}
        first, last = 0, len(num) - 1
        while first <= last:
            if num[last] not in myHash or myHash[num[last]] != num[first]:
                return False
            first += 1
            last -= 1
        return True
