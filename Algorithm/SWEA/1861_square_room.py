def finding_rooms(y,x):
    global cnt
    for a,b in [[y+1, x], [y, x+1], [y-1, x], [y, x-1]]:
        if 0 <= a < N and 0 <= b < N:
            if rooms[y][x] == rooms[a][b] - 1:
                cnt += 1
                finding_rooms(a, b)

test_case = int(input())
for tc in range(1,test_case+1):
    N = int(input())
    rooms = [ list(map(int,input().split())) for _ in range(N) ]

    maximum = 0
    minimum_height = 10000

    for i in range(N):
        for j in range(N):
            cnt = 0
            finding_rooms(i,j)
            if cnt >= maximum:
                if cnt > maximum:
                    minimum_height = rooms[i][j]
                    maximum = cnt
                else:
                    if minimum_height > rooms[i][j]:
                        minimum_height = rooms[i][j]
            # while True:
            #     for a, b in [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]:
            #         if 0 <= a < N and 0 <= b < N:
            #             if rooms[i][j] == rooms[a][b] - 1:
            #                 cnt += 1
            #                 i = a; j = b
            #                 continue
            #     if maximum <= cnt:
            #         start.append(rooms[i][j] - cnt)
            #         maximum = cnt
            #         break
            #     else:
            #         break
    print(f'#{tc} {minimum_height} {maximum + 1}')
