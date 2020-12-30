"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        # This is Time complexity O(n) and Space (1)
        if len(nums) == 1: 
            return nums[0]
        current = nums[0]
        count = 0
        
        for c in nums:
            if current == c: count += 1
            else:
                count -=1 
                if not count:
                    current = c
                    count = 1
        return current
    """
        myDict = {}
        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        return max(myDict.keys(), key=myDict.get)
    # Time and Space is O(n)
    """
        
                
            
    
            