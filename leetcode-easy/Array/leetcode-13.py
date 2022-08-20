class Solution:
    def romanToInt(self, s: str) -> int:
        # RIGHT TO LEFT
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        answer = 0
        index = len(s) - 1
        while index >= 0:
            if index - 1 >= 0 and symbols[s[index]] > symbols[s[index - 1]]:
                answer += (symbols[s[index]] - symbols[s[index - 1]])
                index -= 2
            else:
                answer += symbols[s[index]]
                index -= 1
        return answer

    # LEFT TO RIGHT
    def romanToInt2(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        answer = 0
        i = 0
        while i < len(s):
            # Subtractive case
            if i + 1 < len(s) and symbols[s[i]] < symbols[s[i + 1]]:
                answer += (symbols[s[i + 1]] - symbols[s[i]])
                i += 2
            # Not subtractive case
            else:
                answer += symbols[s[i]]
                i += 1
        return answer
