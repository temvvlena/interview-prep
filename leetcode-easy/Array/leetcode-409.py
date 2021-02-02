"""
https://leetcode.com/problems/longest-palindrome/
Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
"""
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Start adding letters to a set. If a given letter not in the set, add it. 
        If the given letter is already in the set, remove it from the set.
        If the set isn't empty, you need to return length of the string minus 
        length of the set plus 1.
        Otherwise, you return the length of the string (example 'bb.' Your set 
        is empty, you just return 2).
        Essentially, your set contains non-paired letters. It's one of those bad 
        questions where you need to go over all possible cases and somehow fit 
        them into the solution.
        abccccdd
             |
        mySet(a,b, )
        Time and Space Complexity is O(N)
        """
        ans = 0
        for v in Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
        """
        My Solution 
        mySet = set()
        for i in s:
            if i not in mySet: mySet.add(i)
            else: mySet.remove(i)
        if len(mySet) != 0: return len(s)-len(mySet)+1
        else: return len(s)
        """
        
            