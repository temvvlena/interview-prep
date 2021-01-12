"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

"""

class Solution:
    def removeVowels(self, s):
        return "".join(list(filter(lambda ch: ch not in ["a", "e", "i", "o", "u"], s)))