'''
N, K = map(int,input().split())
temp = list(map(int,input().split()))

i = 0; maximum = 0
while i < N:
    ans = sum(temp[i:i+K])
    if maximum < ans:
        maximum = ans
    i += 1
print(maximum)
'''

N, K = map(int, input().split())
arr = list(map(int, input().split()))
Sum = sum(arr[0:K])
ans = Sum
for i in range(1, N-K+1):
    Sum -= arr[i-1]
    Sum += arr[i+(K-1)]
    if ans < Sum:
        ans = Sum

print(ans)