n = int(input())
dp = [1] * (n+1)
for index in range(1, n+1) :
  dp[index] =  (dp[index-1] * index)
result = 1
for index in range(1, n+1) :
  result += 1 / dp[index]
print(result)