"""
Time Complexity O(N)
Space Complexity O(1)
"""

class Solution:
    def myAtoi(self, s) :
        x:int = 0
        multiplier:int = 1
        multiplier_is_set:bool = False
        for c in s:
            if c == " ":
                if multiplier_is_set: break
            if c in ["+","-"]: 
                if multiplier_is_set: break
                else: 
                    multiplier = int(c+"1")
                    multiplier_is_set = True
            if c == ".": break
            if c.isalpha(): break
            if c.isnumeric(): 
                x = x * 10 + int(c)
                multiplier_is_set = True 

        x = x * multiplier
        if x >= 2 ** 31: return 2 ** 31 - 1 
        if x < - 2 ** 31: return - 2 ** 31
        return x
