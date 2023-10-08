import copy

r, c1, c2 = map(int,input().split())
left = [list(map(int,input())) for _ in range(r)]
right = [list(map(int,input())) for _ in range(r)]

ans = "No"
if c1 == c2 == 1:
    ans = "Yes"
else:
    for tx in range(2*c2+c1):
        test = copy.deepcopy(left)
        for y in range(r):
            test[y] = [0] * (c2-2) + test[y] + [0] * c2
        able = True
        for ny in range(r):
            for nx in range(c2):
                if tx + nx >= 2*c2 + c1 - 2:
                    break
                test[ny][tx+nx] += right[ny][nx]
                if test[ny][tx+nx] == 2:
                    able = False
                    break
            if not able:
                break
        if not able:
            continue
        else:

            squareLen = 0
            for ty in range(r):
                squareLen = max(sum(test[ty]), squareLen)

            for y in range(r):
                for x in range(squareLen):
                    if test[y][c2-2+x] == 0:
                        able = False
                        break
                if not able:
                    break

            if not able:
                continue
            else:
                ans = "Yes"
                break
print(ans)
# for x in range(-(c2),c2+1):
#     print(x)
#     test = copy.deepcopy(left)
#     for y in range(r):
#         test[y] += [0] * c2
#     testLen = c1 + c2
#     able = True
#     for ny in range(r):
#         for nx in range(c2):
#             if nx + x >= testLen:
#                 break
#             elif nx + x < 0:
#                 continue
#             test[ny][nx+x] += right[ny][nx]
#             if test[ny][nx+x] == 2:
#                 able = False
#                 break
#         if not able:
#             break
#     if not able:
#         continue
#     else:
#         squareLen = 0
#         for ty in range(r):
#             squareLen = max(sum(test[ty]), squareLen)
#         for Y in range(r):
#             for X in range(squareLen):
#                 if test[Y][X] == 0:
#                     able = False
#                     break
#             if not able:
#                 break
#         if not able:
#             continue
#         else:
#             ans = "Yes"
#             break
# print(ans)