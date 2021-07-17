"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""
class Solution:
    def countSetBits(self, n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count

    def encode(self, string):
        res = 0
        for i in string:
            temp = ord(i) - ord('a')
            res |= 1 << temp
        return res
    
    def helper(self, index, myList, concatenation):
        # base case
        if index == len(myList):
            return self.countSetBits(concatenation)
        # two types.
        res = 0
        # unique baina gesen ug
        if myList[index] & concatenation == 0:
            res = self.helper(index+1, myList, concatenation | myList[index])
        res = max(res, self.helper(index+1, myList, concatenation))
        return res
    
    def unique(self, string):
        return len(set(string)) == len(string)
        
    def maxLength(self, arr: List[str]) -> int:
        # edge case
        if len(arr) == 1: return len(arr[0])
        myList = []
        # encode hiih ystoi
        for i in arr:
            if self.unique(i):
                myList.append(self.encode(i))
        
        return self.helper(0, myList, 0)        