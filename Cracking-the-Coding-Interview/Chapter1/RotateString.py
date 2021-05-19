"""
https://leetcode.com/problems/rotate-string/
Rotate String
We are given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        waterbottle
        erbottlewat
        erbottlewaterbottlewat 
        abcde
        abcedabced
        Time Complexity O(N)
        Space Complexity O(1)
        """
        if len(A) == 0 and len(B) == 0: return True
        if len(A) == 0 and len(B) != 0: return False
        if len(A) != 0 and len(B) == 0: return False
        if len(A) > len(B): return False
        if A == B: return True
        B += B #Time O(N)
        return A in B
        
        # Overall N^2
        # Space N   --> Almost Constant
        """
        if len(A) == 0 and len(B) == 0: return True
        if len(A) == 0 and len(B) != 0: return False
        if len(A) != 0 and len(B) == 0: return False
        i = 0 
        A = list(A) # O(N)
        B = list(B) # O(N)
        while i <= len(A): # O(N)
            temp = A.pop(0) # O(N)
            A+=temp
            if A==B: return True
            i += 1
        return False
        """