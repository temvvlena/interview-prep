# https://leetcode.com/problems/decode-string/
# Time Comlexity and Space O(n)
def decodeString(s):
    myStack, currentCounter, currentStr = [], 0, ''
    for c in s: 
        if c == '[':
            myStack.append(currentStr)
            myStack.append(currentCounter)
            currentStr = ''
            currentCounter = 0
        elif c == ']':
            count = myStack.pop()
            prevStr = myStack.pop()
            currentStr = prevStr + count*currentStr 
        elif c.isnumeric():
            currentCounter = currentCounter * 10 + int(c)
        else:
            currentStr += c
    return currentStr
print(decodeString('31[a2[bc]]'))