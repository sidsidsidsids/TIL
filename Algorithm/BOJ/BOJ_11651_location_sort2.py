N = int(input())
locations = []
for _ in range(N):
    x, y = map(int,input().split())
    locations.append([x, y])

locations.sort(key = lambda X : (X[1], X[0]))

for i in range(N):
    print(*locations[i])