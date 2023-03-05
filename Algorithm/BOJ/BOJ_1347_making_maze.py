n = int(input())
actions = input()
act_f = actions.count('F')

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

a = 0 ; b = 0
min_a = 0 ; min_b = 0 ; max_a = 0 ; max_b = 0
idx = 0
memory = [[] for _ in range(act_f+1)]
memory[0] = [0,0]
m_idx = 1

for i in range(n):
    if actions[i] == 'R':
        idx += 1
        if idx == 4:
            idx = 0
    elif actions[i] == 'L':
        idx -= 1
        if idx == -1:
            idx = 3
    else:
        a += di[idx]
        b += dj[idx]
        memory[m_idx] = [a,b]
        m_idx += 1

        if a > max_a:
            max_a = a
        elif a < min_a:
            min_a = a

        if b > max_b:
            max_b = b
        elif b < min_b:
            min_b = b

garo = max_b - min_b + 1; sero = max_a - min_a + 1
maze = [ ['#'] * garo for _ in range(sero) ]

s = 0
for i in range(sero):
    if s == 1:
        break
    for j in range(garo):
        if s == 1:
            break
        for y, x in memory:
            if i+y < 0 or i+y >= sero or j+x < 0 or j+x >= garo:
                break
        else:
            start_i = i
            start_j = j
            for y, x in memory:
                maze[i+y][j+x] = '.'
            s = 1

for i in range(sero):
    print(''.join(maze[i]))
