'''
1만 있는 줄은 안치기 -> 1이 아닌 값이 있는 줄들을 다 쳐보기?
벽돌 깨는 것을 어떻게 구현할지 (차르봄바, 남은 박스 중력 적용)
한번 하고 맵 복구는 어떻게 할것인지 (V?
'''

def finding_root(board): # 깰 줄(j) 찾기
    target = []

    for i in range(w):
        if sum(board[i]) != board[i].count(1):
            target.append(i)

    return target

def breaking(i,j,k):
    pass



t = int(input())
for tc in range(1, 1+t):
    n, w, h = map(int,input().split())
    grid = [ list(map(int,input().split())) for _ in range(H) ]

