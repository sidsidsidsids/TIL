N, M = map(int,input().split())
numbers = list(map(int,input().split()))

numbers.sort()
bit = [0] * M

def f(i,k):
    if i == k:
        print(*bit)
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
