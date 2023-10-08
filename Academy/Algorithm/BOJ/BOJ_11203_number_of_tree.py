N, path = input().split()
N = int(N)
tree = [[] for _ in range(N+1)]
for n in range(2**(N+1)-1,0,-1):
    tree[len(bin(n)[2:]) - 1].append(2**(N+1)-n)
print(tree)
i = 0
j = 0
for x in range(len(path)):
    if path[x] == "L":
        i += 1
        j += 1+x
    elif path[x] == "R":
        i += 1
        j += x-1

print(tree[i][j])
