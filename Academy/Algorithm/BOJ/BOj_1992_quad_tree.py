N = int(input())
video = [ list(map(int,input())) for _ in range(N) ]

c_video = []

def compression(a,b,grid):
    com_range = (b-a+1)//2
    cnt = 0

    for i in range(com_range):
        for j in range(com_range):
            if grid[i][j] == 0:
                cnt += 1

    if cnt == com_range**2:
        return c_video.append(0)
    elif cnt == 0:
        return c_video.append(1)
    else:
        compression(n//2,grid)

compression