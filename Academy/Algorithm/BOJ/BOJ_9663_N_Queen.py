n = int(input())
loc = [0] * n
ans = 0

def check(x):
    for i in range(x):
        if loc[x] == loc[i] or abs(loc[x] - loc[i]) == x - i:
            return False
    return True

def dfs(x):
    global ans
    if x == n:
        ans += 1
    else:
        for i in range(n):
            loc[x] = i
            if check(x):
                dfs(x+1)

dfs(0)
print(ans)
