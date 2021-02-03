"""
https://leetcode.com/problems/integer-to-roman/
Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
# Time and Space Complexity is O(1) because 1 <= num <= 3999
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        ans = []
        while num:
            for i in romans:
                if num // i[0] > 0:
                    ans.append((num // i[0])*i[1])
                    num %= i[0]
                else: continue
        return "".join(ans)