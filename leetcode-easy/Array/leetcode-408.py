"""
https://leetcode.com/problems/valid-word-abbreviation/submissions/
408. Valid Word Abbreviation
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0': return False
                counter = 0
                while j < len(abbr) and abbr[j].isdigit():
                    counter = counter * 10 + int(abbr[j])
                    test = str(counter)
                    c = 0
                    for num in test:
                        if num == "0": c += 1
                    if c >= 2: return False
                    j += 1
                i += counter
            else:
                if abbr[j] != word[i]:
                    return False
                else:
                    i += 1
                    j += 1
        if i != len(word) or j != len(abbr): return False
        return True
