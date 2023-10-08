computers = int(input())
networks = int(input())
adjL = [ [] for _ in range(computers + 1)]
for _ in range(networks):
    start, finish = map(int,input().split())
    adjL[start].append(finish)
    adjL[finish].append(start)

def virus(start_computer):
    visited = [0] * (computers+1)
    Q = [start_computer]
    visited[start_computer] = -1

    while Q:
        host = Q.pop(0)
        for infect in adjL[host]:
            if visited[infect] == 0:
                visited[infect] = 1
                Q.append(infect)

    return visited.count(1)

print(virus(1))