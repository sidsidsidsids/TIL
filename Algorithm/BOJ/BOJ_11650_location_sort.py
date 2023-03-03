test_case = int(input())
arr = []
for _ in range(test_case):
    x, y = map(int,input().split())
    arr.append([x,y])

arr.sort(key=lambda X : [X[0], X[1]])

for i in range(len(arr)):
    print(*arr[i])