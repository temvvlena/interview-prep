def convertBaseToInt(number):
    def dfs(number, res):
        if number == 0: return res
        res = str(number % 2) + res
        return dfs(number // 2, res)

    return dfs(number, "")


print(convertBaseToInt(233))
