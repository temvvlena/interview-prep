"""
https://leetcode.com/problems/find-common-characters/
10002 Find Common Characters
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for word in words:
            newCheck = []
            for eachElement in word:
                if eachElement in check:
                    newCheck.append(eachElement)
                    check.remove(eachElement)
            check = newCheck
        return check
