"""
https://leetcode.com/problems/degree-of-an-array/submissions/
697. Degree of an Array
"""


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        left, right, counter = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            counter[x] = counter.get(x, 0) + 1
        ans = len(nums)
        degree = max(counter.values())
        for aKey, aValue in counter.items():
            if aValue == degree:
                ans = min(ans, right[aKey] - left[aKey] + 1)
        return ans
        """
        TIME LIMIT EXCEEDED
        {1:2, 2:2, 3:1}
        0  1. 2. 3. 4
        1, 2, 2, 3, 1
                    ^
              ^

        if len(nums) == 1: return 1
        maxNumbersFreq = []
        for i in range(len(nums)):
            counter = 0 
            temp = 0
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                if nums[j] == nums[i]:
                    counter += 1
                    temp = max(temp, j-i+1)

            maxNumbersFreq.append([counter, temp])
        maxNumbersFreq.sort(key = lambda x: x[0], reverse=True)
        res = []
        maxCounter = maxNumbersFreq[0][0]
        for counter, freq in maxNumbersFreq:
            if counter == maxCounter:
                res.append(freq)
        return min(res)
        """
