N, M = map(int,input().split())
bit = [0] * M

numbers = list(map(int,input().split()))
numbers.sort()

visit = [1] * N

def f(i,k,v):
    if i == k:
        print(*bit)
    else:
        for j in range(N):
            if v[j]:
                bit[i] = numbers[j]
                v[j] = 0
                f(i+1, k, v)
                bit[i] = 0
                v[j] = 1

f(0,M,visit)