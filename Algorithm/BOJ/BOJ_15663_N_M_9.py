import sys
input = sys.stdin.readline

N, M = map(int,input().split())
numbers = list(map(int,input().split()))

bit = [0] * M
result = set()
visit = [1] * N
def f(i,k,v):
    global result

    if i == k:
        res = [0] * M
        for n in range(M):
            res[n] += bit[n]
        result.add(tuple(res))

    else:
        for j in range(N):
            if v[j]:
                bit[i] = numbers[j]
                v[j] = 0
                f(i+1,k,v)
                bit[i] = 0
                v[j]=1


f(0,M,visit)

result = sorted(result)
for r in result:
    print(*r)
