"""
https://leetcode.com/problems/design-compressed-string-iterator/
"""


class StringIterator:

    def __init__(self, compressedString: str):
        def flattenString(text):
            res = []
            num = 0
            for char in text:
                if char.isnumeric():
                    num = num * 10 + int(char)
                elif num == 0:
                    res.append(char)
                else:
                    temp = res.pop()
                    temp *= num
                    res.append(temp)
                    res.append(char)
                    num = 0
            if num != 0:
                temp = res.pop()
                temp *= num
                res.append(temp)
                num = 0
            return ''.join(res)

        self.myString = flattenString(compressedString)
        self.position = -1

    def next(self) -> str:
        self.position += 1
        try:
            return self.myString[self.position]
        except:
            return " "

    def hasNext(self) -> bool:
        return len(self.myString) - 1 > self.position

    # Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
