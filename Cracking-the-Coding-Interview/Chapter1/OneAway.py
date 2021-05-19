"""
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

Example
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False

Hint number 1. How to individually check insert, remove, and replace? 

Time Complexity O(N) and Space Complexity O(1)
"""
def oneway(string1, string2):

    l1 = len(string1)
    l2 = len(string2)
    if abs(l1 - l2) >= 2: return False

    if l1 == l2: return equalLength(string1, string2)
    elif l1+1 == l2: return oneCheck(string1, string2)
    elif l1-1 == l2: return oneCheck(string2, string1)

def oneCheck(s1, s2):
    i = 0 
    j = 0 
    count = 0 
    while i <= len(s1) - 1 and j <= len(s2) - 1:
        if s1[i] != s2[j]:
            count += 1
            if count == 2: return False
            j += 1
        i += 1
        j += 1
    return True

def equalLength(s1, s2):
    i = 0
    count = 0
    while i <= len(s1)-1:
        if s1[i]!=s2[i]:
            count += 1
            if count == 2:
                return False
        i += 1
    return True

print(oneway("pale", "ple"), "True")
print(oneway("pales", "pale"), "True")
print(oneway("pale", "bale"), "True")
print(oneway("pale", "bake"), "False")