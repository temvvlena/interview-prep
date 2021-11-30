"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

# Most Optimal Solution


class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        """
        1,2,3,4,5,6,7
        ^           ^
        """
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        1,2,3,4,5,6,7
        7,6,5,4,3,2,1
        5,6,7,1,2,3,4
        """
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        return nums


"""
class Solution:
    def rotate(self, nums, k):
        
        Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
      
        for i in range(k):
            temp = nums[-1]
            nums.insert(0, nums[-1])
            nums.pop()
        return nums
"""
