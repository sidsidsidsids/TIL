N, M = map(int,input().split())
bit = [0] * M
numbers = [0] * N
for n in range(1,1+N):
    numbers[n-1] = n

def f(i, k):
    if i == k:
        print(*bit)
    else:
        for j in range(N):
            if i > 0:
                if bit[i-1] <= numbers[j]:
                    bit[i] = numbers[j]
                    f(i+1,k)
                else:
                    continue
            else:
                bit[i] = numbers[j]
                f(i+1,k)
                bit[i] = 0

f(0,M)