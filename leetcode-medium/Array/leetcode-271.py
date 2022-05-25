"""
https://leetcode.com/problems/encode-and-decode-strings/
Encode and Decode Strings
"""


class Codec:
    """
    [Hello,World]
      ^
    12-1232-232-123-123$99-2-3-4-1-2-3
    [12-1232-232-123-123, 99-2-3-4-1-2-3]
    [12, 1232, 232, 123, 123]
    """

    def encodeWord(self, word):
        temp = []
        if word == "":
            return '10000'
        for index in range(len(word)):
            temp.append(str(ord(word[index])))
            temp.append('-')
        if len(temp) != 0:
            temp.pop()
        return ''.join(temp)

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedString = []
        for value in strs:
            encodedWord = self.encodeWord(value)
            encodedString.append(encodedWord)
            encodedString.append("$")
        if len(encodedString) != 0:
            encodedString.pop()
        return "".join(encodedString)

    def decodeWord(self, word: str):
        # 12-1232-232-123-123
        if word == "10000":
            return ''
        s = word.split('-')
        res = []
        for i in s:
            temp = chr(int(i))
            res.append(temp)
        return "".join(res)

    # "12-1232-232-123-123$99-2-3-4-1-2-3"
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        s = s.split('$')  # array boltson
        res = []
        for value in s:
            decodedWord = self.decodeWord(value)
            res.append(decodedWord)
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
