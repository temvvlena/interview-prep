"""
https://leetcode.com/problems/valid-palindrome/
Valid Palindrome
Given a string, determine if it is a palindrome, considering only 
alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as 
valid palindrome.
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s):
        # First Solution is Time and Space O(N)
        if s == '': return True
        s = s.lower()
        res = ''
        for i in s:
            if i.isdigit() or i.isalpha():
                res += i
        return res == res[::-1]
                
        # Can I make it Space O(1)? Using two pointers?