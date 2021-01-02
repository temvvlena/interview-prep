class Solution:
    def isValid(self, s):
        mStack = []
        
        """
        { { } [ ] [ [ [ ] ] ] }
          { } [ ]
                  [ [ [ ] ] ] 
        """
        closingC = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closingC:
                try:
                    top = mStack.pop()
                except:
                    return False
                if closingC[c] != top:
                    return False
            else:
                mStack.append(c)
        return len(mStack) == 0
        # Big(O) time & space = N