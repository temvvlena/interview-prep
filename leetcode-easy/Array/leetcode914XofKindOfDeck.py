"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
X of a Kind in a Deck of Cards
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
"""
class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v%X==0 for v in count.values()):
                    return True
        return False
"""
{1:2, 2:2, 3:2, 4:2} --> True
{1:3, 2:3, 3: 2} --> False
[1] -> False
{1:2} --> 
[0,0,0,1,1,1,1,1,1,2,2,2,3,3,3]
[1,1,1,2,2,2,3,3,3]
"""