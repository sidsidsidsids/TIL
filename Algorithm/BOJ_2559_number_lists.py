
N, K = map(int,input().split())
temp = list(map(int,input().split()))

i = 0; maximum = 0
while i < N:
    ans = sum(temp[i:i+K])
    if maximum < ans:
        maximum = ans
    i += 1
print(maximum)