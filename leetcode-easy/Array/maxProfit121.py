"""
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""

# Get the first val 
# From the second val, I can compare it with the min val.
# If it's greater than the min value, I return the max of ans and the differences
# else, update the min value

class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        if not prices:
            return 0
        else:
            mini = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < mini:
                    mini = prices[i]
                else:
                    ans = max(ans, prices[i] - mini)
            return ans
    