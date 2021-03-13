"""
https://leetcode.com/problems/valid-palindrome-ii/
Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
Time O(N) space (1)
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValindrome(string, left, right, k):
            while left < right:
                if string[left] != string[right]:  
                    if k == 0: return False
                    return isValindrome(s, left+1, right, k-1) or isValindrome(s, left, right-1,  k-1)
                left += 1
                right -= 1
            return True
        return isValindrome(s, 0, len(s)-1, 1)