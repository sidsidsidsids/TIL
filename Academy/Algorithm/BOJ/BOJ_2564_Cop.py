'''
1 : 0, 4
2 : 2, 0
3 : 5, 8
동근 : 5, 3
'''
garo, sero = map(int,input().split())
# 집 
store = int(input())
L_list = []
K_list = []
for _ in range(store):
    L, K = map(int,input().split())
    L_list.append(L)
    K_list.append(K)

# 경비
L, K = map(int,input().split())

# 거리 계산 (1 위 2 아래 3 왼쪽 4 오른쪽)
dist = 0
for i in range(store):
    if L == 1:
        if L_list[i] == 1:
            dist += abs(K_list[i] - K)
        elif L_list[i] == 2:
            dist += min(sero + K_list[i] + K, sero + (garo - K_list[i]) + (garo - K))
        elif L_list[i] == 3:
            dist += K + K_list[i]
        elif L_list[i] == 4:
            dist += (garo - K) + K_list[i]
    elif L == 2:
        if L_list[i] == 1:
            dist += min(sero + K_list[i] + K, sero + (garo - K_list[i]) + (garo - K))
        elif L_list[i] == 2:
            dist += abs(K_list[i] - K)
        elif L_list[i] == 3:
            dist += K + (sero - K_list[i])
        elif L_list[i] == 4:
            dist += (garo - K) + (sero - K_list[i])
    elif L == 3:
        if L_list[i] == 1:
            dist += K + K_list[i]
        elif L_list[i] == 2:
            dist += (sero - K) + K_list[i]
        elif L_list[i] == 3:
            dist += abs(K_list[i] - K)
        elif L_list[i] == 4:
            dist += min(K + garo + K_list[i], (sero - K) + garo + (sero - K_list[i]))
    elif L == 4:
        if L_list[i] == 1:
            dist += K + (garo - K_list[i])
        elif L_list[i] == 2:
            dist += (sero - K) + (garo - K_list[i])
        elif L_list[i] == 3:
            dist += min(K + garo + K_list[i], (sero - K) + garo + (sero - K_list[i]))
        elif L_list[i] == 4:
            dist += abs(K_list[i] - K)

print(dist)


