from itertools import combinations

N, M = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]

chicken = [];
home = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            chicken.append([i,j])
        elif grid[i][j] == 1:
            home.append([i,j])

#c_len = len(chicken)
h_len = len(home)
# temp = [0] * c_len
# v = [0] * c_len
# comb = []
#
# def c_comb(i,k,visit):
#     if i == k:
#         t_comb = [0] * M
#         for l in range(M):
#             t_comb[l] = temp[l]
#         t_comb.sort(key=lambda X:(X[0], X[1]))
#         if t_comb not in comb:
#             comb.append(t_comb)
#         return
#     else:
#         for j in range(c_len):
#             if not visit[j]:
#                 temp[i] = chicken[j]
#                 visit[j] = 1
#                 c_comb(i+1,k,visit)
#                 temp[i] = 0
#                 visit[j] = 0
#
# c_comb(0,M,v)

subset = list(combinations(chicken,M))

def c_dist(chickenss,homes):
    min_cnt = 2*N*h_len
    for chickens in chickenss:
        cnt = 0
        for home in homes:
            c_dist_all = [0] * M
            idx = 0
            for store in chickens:
                c_dist_all[idx] += abs(home[0] - store[0]) + abs(home[1]-store[1])
                idx += 1
            cnt += min(c_dist_all)
            if cnt > min_cnt:
                break
        if min_cnt > cnt:
            min_cnt = cnt
    return min_cnt

ans = c_dist(subset,home)

print(ans)

