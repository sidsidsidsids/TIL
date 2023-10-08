import sys
input = sys.stdin.readline

N, M = map(int,input().split())
numbers = list(map(int,input().split()))

result = set()
bit = [0] * M

def f(i,k):
    global result

    if i == k:
        res = [0] * M
        for n in range(M):
            res[n] += bit[n]
        result.add(tuple(res))
    else:
        if i == 0:
            for j in range(N):
                bit[i] = numbers[j]
                f(i+1,k)
        else:
            for j in range(N):
                if bit[i-1] <= numbers[j]:
                    bit[i] = numbers[j]
                    f(i+1,k)

f(0,M)

result = sorted(result)
for r in result:
    print(*r)
