"""
https://leetcode.com/problems/permutations-ii/
Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n: 
                if nums[:] not in output:
                    output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i]=nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i]=nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack()
        return output