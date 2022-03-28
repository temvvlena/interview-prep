def iterate(nums):
    """
    [[1,2,3],
     [4,5],
     [6],
     [],
     [7,8,9]] ---> [1,4,6,7,2,5,8,3,9]
      ^
    """
    res = []
    col = 0
    n = len(nums)
    for col in range(1000):
        temp = False
        for row in range(n):
            if len(nums[row]) > col:
                res.append(nums[row][col])
                temp = True
        if temp is False:
            return res
print(iterate([[1,2,3],[4,5],[6],[],[7,8,9]]))
print(iterate([[],[1],[2],[],[7,8,9,10]]))





