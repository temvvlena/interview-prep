"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:

Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
"""

import string
class Solution:
    def modifyString(self, s: str) -> str:
        temp_original = set(string.ascii_lowercase)
        res = list(s)
        for i in range(len(res)):
            if res[i] == "?":
                temp = temp_original.copy()
                if i > 0: temp.discard(res[i-1])
                if i< len(res)-1: temp.discard(res[i+1])
                res[i] = temp.pop()
            else: res[i] = s[i]
        return "".join(res)