N = int(input())
nums = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):
        if nums[i] >= nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp) + 1)