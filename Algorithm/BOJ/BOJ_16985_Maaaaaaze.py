maze = [[list(map(int,input().split())) for _ in range(5)] for __ in range(5)]

print(maze[0])
'''
구현할 거
- 판 돌리기
- 돌은 판에 따른 구현 가능 미로 4**5개
- 각 판에 대한 BFS
'''

def maze_init(maze_board):
    change1 = [[0] * 5] * 5
    change2 = [[0] * 5] * 5
    change3 = [[0] * 5] * 5
    for i in range(5):
        for j in range(5):
            if maze_board[i][j] == 1:
                change1[-(j-1)][-(i-1)] = 1
                change2[-(i-1)][-(j-1)] = 1
                change3[-(j-1)][-i] = 1
    return maze_board, change1, change2, change3
a,b,c,d = maze_init(maze[0])
print(a,b,c,d)
