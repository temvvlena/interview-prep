"""
Implement a method to perform basic string compression using the counts of repeated chatacters. 
For example, the string aabccccaaa would become a2b1c5a3. If the "compressed" string would not
become smaller than the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).

["a", 2, "b", 1, "c", 3, "a", 3]
aabccccaaa
   ^
  ^
    # pseudocode
    initialize a list
    left
    iterate throught the string
        if right pointer is not equal to the left pointer
            slice the string and then add it onto the the list
            increase the left pointer
    return the list as a string
    aabccccaaa
    ^
      ^
"""
def compress(compressedString):
    if len(compressedString) == 1: return compressedString
    compressedList = []
    leftPointer = 0 
    rightPointer = 0 
    counter = 0 
    while rightPointer <= len(compressedString) - 1:
        if compressedString[rightPointer] != compressedString[leftPointer]:
            compressedList.append(compressedString[leftPointer])
            compressedList.append(counter)
            counter = 0 
            leftPointer = rightPointer
        counter += 1
        rightPointer += 1
    compressedList.append(compressedString[leftPointer])
    compressedList.append(counter)
    res = ""
    for i in compressedList:
        res+=str(i)
    return res
print(compress("aabccccaaa"))
print(compress("aaaaaaa"))
print(compress("aaaaaaab"))

