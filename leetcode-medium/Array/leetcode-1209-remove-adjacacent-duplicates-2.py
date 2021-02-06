"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Remove All Adjacent Duplicates in String II
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
Time and Space Complexity O N
"""
class Pair:
    def __init__(self, letter=None, count=0):
        self.letter = letter
        self.count = count
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:    
        myList, anotherList = list(s), list()
        for i in range(0, len(myList)):
            if anotherList == []: 
                anotherList.append(Pair(myList[i], 1))
                continue
            if anotherList[-1].letter == myList[i]:
                anotherList[-1].count += 1
                if anotherList[-1].count == k: anotherList.pop()
            else: anotherList.append(Pair(myList[i], 1))
        s=''
        for i in anotherList: s += (i.letter*i.count)
        return s