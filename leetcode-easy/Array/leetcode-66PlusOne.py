"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
"""


# If the last element is 9 make it 0. Else, add 1. After that, return [1] + digits will make it [1, 0]
# Time complexity : N
# Space complexity : N. If it contains 9 else 1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [0]: return [1]
        i = len(digits) - 1
        while i >= 0:
            temp = digits[i]
            if temp == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        return [1] + digits


"""
Bruto Force

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for num in digits:
            res+=str(num)
        ans = int(res) + 1
        ans = str(ans)
        out = []
        for i in ans:
            out.append(int(i))
        return out
"""
