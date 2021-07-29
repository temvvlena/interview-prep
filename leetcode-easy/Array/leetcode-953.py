
"""
Time Complexity: O(C), where C is the total content of words.

Space Complexity: O(1).
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myHash = {}
        for i in range(len(order)): myHash[order[i]] = i
        def helper(word1, word2):
            index = 0
            while index <= len(min(word1, word2))-1:
                if myHash[word1[index]] > myHash[word2[index]]: return False 
                if myHash[word1[index]] < myHash[word2[index]]: return True  
                index += 1
            if index < len(word1): return False
            return True
        firstPointer = 0
        while firstPointer < len(words)-1:
            if helper(words[firstPointer], words[firstPointer+1]) is False: return False
            firstPointer += 1
        return True
                          
        