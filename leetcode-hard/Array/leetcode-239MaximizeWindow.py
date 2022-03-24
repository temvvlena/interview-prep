"""
https://leetcode.com/problems/sliding-window-maximum/
Sliding Window Maximum
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

        """
        My Solution: Bruto Force Solution. Time Complexity KN
        if k == 1: return nums
        left, right, res, maxNum,temp = 0, 0, [], 0, []
        while left+k <= len(nums):
            if right-left == k-1:
                left += 1
                res.append(max(temp))
                temp = []
            maxNum = max(nums[left:right+2])
            temp.append(maxNum)
            maxNum = 0
            right += 1
        return res
        """
