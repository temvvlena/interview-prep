class Solution:
    
    def __init__(self):
        self.res = []
    
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(numRows):
            temp = []
            if numRows == 1: temp.append(1)
            else:
                li = helper(numRows-1)
                temp = []
                for i in range(1, len(li)):
                    temp.append(li[i-1]+li[i])
                temp.insert(0, 1)
                temp.append(1)
            self.res.append(temp)
            return temp
        if numRows == 0: return []
        helper(numRows)
        return self.res
        
    
    