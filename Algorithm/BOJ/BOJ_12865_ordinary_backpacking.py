n, limit = map(int,input().split())
W = [0] * n
V = [0] * n

for i in range(n):
    w, v = map(int,input().split())
    W[i] = w
    V[i] = v

minW = min(W)
max_value = 0
visit = [0] * n

def backpacking(weight, value, bag_limit, visited):
    global max_value

    if weight + minW >= bag_limit:
        if weight <= bag_limit:
            if value >= max_value:
                max_value = value
                return
            else:
                return
        else:
            return

    for j in range(n):
        if not visited[j]:
            weight += W[j]
            value += V[j]
            visited[j] = 1
            backpacking(weight, value, bag_limit, visited)
            weight -= W[j]
            value -= V[j]
            visited[j] = 0

backpacking(0,0,limit,visit)

print(max_value)
