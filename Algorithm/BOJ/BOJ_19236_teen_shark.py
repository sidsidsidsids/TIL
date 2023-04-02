'''
상어가 먹음
물고기들 이동
상어가 이동하면서 그 위치 물고기 먹음
물고기들 이동
반복...
상어가 이동할 수 없으면 종료 (이동할 칸에 물고기가 없으면)
'''
fishes = [[0] * 4 for _ in range(4)]

for j in range(4):
    inputs = list(map(int,input().split()))
    for i in range(0,7,2):
        fishes[j][i//2] = [inputs[i], inputs[i+1]]

# print(fishes)

move = [[],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1],[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1]]

def moving(grid):
    move_fish = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            move_fish.append(fishes[i][j])

    move_fish.sort(key=lambda X:X[0])

    for fish in move_fish:
        ny, nx = 



