"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
345. Reverse Vowels of a String
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        first, last = 0, len(s) - 1
        s = [char for char in s]
        vowels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1,
                  "A": 1, "E": 1, "I": 1, "O": 1, "U": 1}
        while first < last:
            if s[first] in vowels and not s[last] in vowels:
                last -= 1
            elif s[last] in vowels and not s[first] in vowels:
                first += 1
            elif s[last] not in vowels and s[first] not in vowels:
                first += 1
                last -= 1
            else:
                s[first], s[last] = s[last], s[first]
                first += 1
                last -= 1
        return "".join(s)
