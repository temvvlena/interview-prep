"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []
"""
# Takes a list and returns list of lists
# Time Complexity O(nLogn * n), so overall O(n^2)
# Main idea here is the same as twoSum, but one should consider duplicates
class Solution:
    def threeSum(self, nums):
        nums.sort() 
        N, result = len(nums), []
        for i in range(N):
            # If the next nums[i] is the same as previous one, why bother?
            if i > 0 and nums[i] == nums[i-1]:
                # it's not pass but continue
                continue
            # It will help a lot if it was positive number than negative
            target = nums[i]*-1
            # Since it's sorted, a will be the first. b + c should be equal to a
            j, k = i+1, N-1
            while j < k:
                if nums[j]+nums[k] == target:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    # Checking duplicates. This is amazing!!
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                # Just as the twoSum, if the target is greater than the sum, j should increase
                elif nums[j] + nums[k] < target:
                    j += 1
                # If less, decreases -= 1. For more info, why its increasing or decreasing.
                # https://www.youtube.com/watch?v=Ca7k53qcTic&ab_channel=KnowledgeCenter
                else:
                    k -= 1
        return result

        