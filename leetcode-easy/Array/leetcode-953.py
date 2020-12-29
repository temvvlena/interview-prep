
"""
Time Complexity: O(C), where C is the total content of words.

Space Complexity: O(1).
"""

class Solution:
    def isAlienSorted(self, words, order) :
        myDictionary = dict()
        for i in range(len(order)):
            myDictionary[order[i]] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if myDictionary[word1[k]] > myDictionary[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True
                          
        