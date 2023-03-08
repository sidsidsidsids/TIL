'''
겹치는 인덱스 [2] [6]
'''
wheel = [ list(map(int,input())) for _ in range(4) ]
tries = int(input())
for _ in range(tries):
    num, direction = map(int,input().split())

    change = [0] * 4
    change[num-1] = direction

    if num == 1:
        if wheel[0][2] != wheel[1][6]:
            change[1] = -direction
        if wheel[1][2] != wheel[2][6] and change[1] != 0:
            change[2] = direction
        if wheel[2][2] != wheel[3][6] and change[2] != 0:
            change[3] = -direction
    elif num == 2:
        if wheel[0][2] != wheel[1][6]:
            change[0] = -direction
        if wheel[1][2] != wheel[2][6]:
            change[2] = -direction
        if wheel[2][2] != wheel[3][6] and change[2] != 0:
            change[3] = direction
    elif num == 3:
        if wheel[2][2] != wheel[3][6]:
            change[3] = -direction
        if wheel[1][2] != wheel[2][6]:
            change[1] = -direction
        if wheel[0][2] != wheel[1][6] and change[1] != 0:
            change[0] = direction
    elif num == 4:
        if wheel[2][2] != wheel[3][6]:
            change[2] = -direction
        if wheel[1][2] != wheel[2][6] and change[2] != 0:
            change[1] = direction
        if wheel[0][2] != wheel[1][6] and change[1] != 0:
            change[0] = -direction

    for i in range(4):
        if change[i] == 1:
            last = wheel[i].pop()
            wheel[i] = [last] + wheel[i]
        elif change[i] == -1:
            first = wheel[i].pop(0)
            wheel[i] = wheel[i] + [first]
        else:
            pass

score = 0
if wheel[0][0] == 1:
    score += 1
if wheel[1][0] == 1:
    score += 2
if wheel[2][0] == 1:
    score += 4
if wheel[3][0] == 1:
    score += 8


print(score)