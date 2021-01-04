"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), 
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs 
that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", 
        "0:08", "0:16", "0:32"]
"""
class Solution:
    _LED_NUM = 10
    _HOUR_LED_NUM = 4

    # Backtracking
    def __init__(self):
        self._times = []

    def readBinaryWatch(self, num: int):
        self._backtrack(num, 0, 0, 0)
        return self._times
    
    def _backtrack(self, num: int, pos: int, hour: int, minute: int):
        if hour > 11 or minute > 59:
            return
        elif num == 0:
            self._times.append("{:d}:{:02d}".format(hour, minute))
            return

        for i in range(pos, Solution._LED_NUM):
            if i < Solution._HOUR_LED_NUM:
                self._backtrack(num - 1, i + 1,
                    hour + 2**i, minute)
            else:
                self._backtrack(num - 1, i + 1,
                    hour, minute + 2**(i - Solution._HOUR_LED_NUM))