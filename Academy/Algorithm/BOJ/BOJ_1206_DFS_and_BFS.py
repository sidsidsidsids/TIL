V, E, S = map(int,input().split())
route = []
for _ in range(E):
    route.append(list(map(int,input().split())))

array = [ [0] * (V+1) for _ in range(V+1) ]
visited_d = visited_b = [0] * (V+1)

for i in range(E):
    v1, v2 = route[i][0], route[i][1]
    array[v1][v2] = 1

def dfs(s):
    visited_d[s] = 1
    print(s, end=' ')

    for t in range(1, V+1):
        if array[s][t] == 1 and visited_d[t] == 0:
            dfs(t)

def bfs(s):
    queue = [s]
    visited = []

    while queue:
        current_node = queue.pop()
        visited.append(current_node)
        print(current_node, end=' ')
        for adjacent_node in array[current_node]:
            print(array[current_node])
            if adjacent_node not in visited:
                queue.append(adjacent_node)
                print(adjacent_node, end=' ')
    return visited

dfs(S)
print('')
bfs(S)