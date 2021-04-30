"""
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        horizontalCuts.append(0)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        maxHeight = 0 
        maxWidth = 0
        for i in range(1, len(horizontalCuts)):
            if horizontalCuts[i] - horizontalCuts[i-1] > maxHeight: maxHeight = horizontalCuts[i] - horizontalCuts[i-1] 
        for i in range(1, len(verticalCuts)):
            if verticalCuts[i] - verticalCuts[i-1] > maxWidth: maxWidth = verticalCuts[i] - verticalCuts[i-1]
        return (maxWidth*maxHeight) % (10**9+7)   