"""
11. Container With Most Water
Given n non-negative integers 
a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 1:
Input: height = [1,1]
Output: 1
Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxArea = 0, len(height) - 1, 0
        while right>left:
            maxArea = max(maxArea, min(height[right], height[left]) * (right-left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return maxArea
        