"""
https://leetcode.com/problems/count-binary-substrings/
Count Binary Substrings
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counter0, counter1, result = 0, 0, 0
        for index in range(len(s)):
            if s[index] == '0':
                counter0 += 1
            if s[index] == '1':
                counter1 += 1
            if index < len(s) - 1 and s[index + 1] != s[index]:
                result += min(counter0, counter1)
                if s[index + 1] == '1':
                    counter1 = 0
                else:
                    counter0 = 0
        result += min(counter0, counter1)
        return result

        """
        0001100011
                ^
        0 -> 3
        1 -> 2
        minimum ni 2 bolomj bn count = 2+2+2 = 6
        """
