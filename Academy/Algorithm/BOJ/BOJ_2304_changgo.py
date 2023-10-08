n = int(input())
buildings = []
maxH = 0
maxH_idx = []
for i in range(n):
    L, H = map(int,input().split())
    if maxH <= H:
        if maxH == H:
            maxH_idx.append(L)
        else:
            maxH_idx = [L]
            maxH = H
    #print()
    buildings.append(L)
    buildings.append(H)


start_idx = min(buildings[0::2])
end_idx = max(buildings[0::2])
changgo = [0] * (end_idx + 1)
for i in range(n):
    changgo[buildings[2*i]] = buildings[2*i + 1]
answer = 0



if len(maxH_idx) > 1:
    left = min(maxH_idx)
    right = max(maxH_idx)

    maxH_tmp = 0
    for i in range(start_idx, left):
        if maxH_tmp < changgo[i]:
            maxH_tmp = changgo[i]
        answer += maxH_tmp
    maxH_tmp = 0
    for i in range(end_idx, right, -1):
        if maxH_tmp < changgo[i]:
            maxH_tmp = changgo[i]
        answer += maxH_tmp

    answer += maxH * (right - left + 1)


else:
    maxH_tmp = 0
    for i in range(start_idx,maxH_idx[0]):
        if maxH_tmp < changgo[i]:
            maxH_tmp = changgo[i]
        answer += maxH_tmp

    maxH_tmp = 0
    for i in range(end_idx,maxH_idx[0],-1):
        if maxH_tmp < changgo[i]:
            maxH_tmp = changgo[i]
        answer += maxH_tmp

    answer += maxH

print(answer)


#print(start_idx, end_idx, maxH_idx, changgo)
