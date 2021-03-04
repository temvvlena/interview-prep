"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""
# Not Done Yet
class Solution:
    def lengthOfLongestSubstring(self, s):
        # abcabcbb
        # When you see a repeating character, append and start counting again
        start = 0
        res = list()
        previous_sub = ""
        maxLength = 0
        
        if s == "":
            return 0
        if s == " ":
            return 1
        while start < len(s):
            if s[start] in previous_sub:
                res.append(previous_sub)
                previous_sub = ''   
            previous_sub += s[start]
            start += 1
        for i in res:
            maxLength = max(maxLength, len(i))
        return maxLength
    
        """
        abcadcbb -> adcb
              ^
        {a:3, b:7, c:5, d:1}
        left = 0
        right = 0
        
        abcabcbb
           ^ 
        {a:1, b:2, c:3, a:4}
               ^         ^
        Time and Space O(N)
        
        right = 0
        left = 0
        myHash = {}
        res = 0
        while right <= len(s)-1:
            if s[right] in myHash: 
                left = max(myHash[s[right]], left)
            res = max(res,right-left+1)
            myHash[s[right]]=right+1
            right += 1
        return res
        """