"""
https://leetcode.com/problems/friends-of-appropriate-ages/
825. Friends Of Appropriate Ages
"""


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = 0
        """
        20 30 100 110 120
        ^
        ^
        Time Limit Exceeded. 
        But Solved it during the phone interview:)
        """
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i == j:
                    continue
                elif ages[i] <= 0.5 * ages[j] + 7:
                    continue
                elif ages[i] > ages[j]:
                    continue
                elif ages[i] > 100 and ages[j] < 100:
                    continue
                else:
                    counter += 1
        return counter
