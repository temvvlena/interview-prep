"""
Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
Given a string text, you want to use the characters of text to form as many instances of 
the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances 
that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""
import collections
class Solution:
    def maxNumberOfBalloons(self, text):
        # Solution 1. Time is O(N) and Space is Constant
        # return min(text.count('b'), text.count('a'), text.count('l') // 2, text.count('o') // 2, text.count('n'))
        
        # Solution 2. Time and Space Complexity O(N)
        MAX_VALUE = 1430
        balloon = "balloon"
        text_map = collections.Counter(text)
        balloon_map = collections.Counter(balloon)
        total = MAX_VALUE
        if len(text) >= len(balloon):             
            for c in balloon_map:
                if c in text_map:
                    max_repeat = text_map[c] // balloon_map[c]
                    if max_repeat <= total: total = max_repeat
                else: total = MAX_VALUE
        if total == MAX_VALUE: return 0
        else: return total