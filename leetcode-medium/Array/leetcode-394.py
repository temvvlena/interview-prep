# https://leetcode.com/problems/decode-string/
# Time Comlexity and Space O(n)
def decodeString(s: str) -> str:
    stack, currentCounter, currentString = [], 0, ''
    for c in s:
        if c == "[":
            stack.append(currentCounter)
            stack.append(currentString)
            currentCounter, currentString = 0, ''

        if c == "]":
            prev = stack.pop()
            counter = stack.pop()
            currentString = prev + counter * currentString

        if c.isnumeric():
            currentCounter = currentCounter * 10 + int(c)

        else:
            currentString += c
    res = []
    for c in currentString:
        if c == "[" or c == ']':
            continue
        res.append(c)
    return "".join(res)


print(decodeString('31[a2[bc]]'))
