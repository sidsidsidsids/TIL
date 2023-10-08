from collections import deque
import sys

N, M = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]

value = 1

next = [(-1,0), (1,0), (0,-1), (0,1)]
Q = deque()
Q.append([0,0,set(board[0][0])])
while Q:
    elem = Q.pop()
    y, x, alphabet = elem[0], elem[1], elem[2]
    for dy, dx in next:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] not in alphabet:
                Q.append([ny,nx,alphabet + board[ny][nx]])

def dfs(r,c,record):


print(value)