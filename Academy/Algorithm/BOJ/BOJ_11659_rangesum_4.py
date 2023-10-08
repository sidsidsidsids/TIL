import sys
input = sys.stdin.readline

N,M = map(int,input().split())
numbers = list(map(int,input().split()))
for i in range(1,N):
    numbers[i] = numbers[i]+numbers[i-1]

for _ in range(M):
    left, right = map(int,input().split())
    if left == 1:
        print(numbers[right-1])
    else:
        print(numbers[right-1]-numbers[left-2])