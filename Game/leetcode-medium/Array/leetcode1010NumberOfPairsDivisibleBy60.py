"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0 
        myDict = [0]*501
        for i in range(len(time)):
            whole = time[i] // 60
            check = abs(whole+1)*60-time[i]
            while check <= 500:
                res += myDict[check]
                check += 60
            myDict[time[i]] += 1
        return res
        """
        count = 0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if (time[i]+time[j])%60 ==0:
                    count += 1
        return count
        """