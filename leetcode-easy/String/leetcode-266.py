"""
Given a string, determine if a permutation of the string could form a palindrome.
Example 1:
Input: "code"
Output: false
Example 2:
Input: "aab"
Output: true
Example 3:
Input: "carerac"
Output: true
"""
class Solution:
    def canPermutePalindrome(self, s):
        # "aab" 
        # {a: 2, b:1}
        # Characteristics:
        """
        To make a palindrome
         - all characters should appear in even numbers
         - except number 1
        """
        myHash = {}
        for i in s:
            if i not in myHash:
                myHash[i] = 1
            else:
                myHash[i] += 1
                # aaa
        counter = 0
        for aValue in myHash.values():
            if aValue % 2 != 0:
                counter += 1
        return counter < 2
        # Time and Space (N)