"""
https://leetcode.com/problems/reverse-string/
Time complexity : O(N) time to perform N/2 swaps.

Space complexity : O(N) to keep the recursion stack.
"""
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
        helper(0, len(s) - 1)
        # ["h","e","l","l","o"]
        # ["o", "e", "l", "l","h"]
        # ["o", "l", "l", "e","h"]

"""
Time complexity : O(N) to swap N/2 element.

Space complexity : O(1), it's a constant space solution.

    
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
"""