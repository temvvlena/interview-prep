"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        counter = 0
        [3,4,7,2,-3,1,4,2,1] k = 7
             ^
         3,7,14,16,13,14,18,21,22
        -4,0,7  9. 6. 7. 11.14.15
         {0:1, 3:1, 7:1, 14:1}
        """
        myDict,preSum,res = {0:1}, 0, 0
        for num in nums:
            preSum += num
            if preSum - k in myDict: res += myDict[preSum - k]
            if preSum in myDict: myDict[preSum] += 1
            else: myDict[preSum] = 1
        return res
