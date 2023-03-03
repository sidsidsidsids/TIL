N, M = map(int,input().split())
dictionary = {}
for _ in range(N):
    site, pw = input().split()
    dictionary[site] = pw
for _ in range(M):
    target = input()
    print(dictionary[target])