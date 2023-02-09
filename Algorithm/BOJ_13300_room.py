student_amount, room_limit = map(int,input().split())
boy = [0] * 6
girl = [0] * 6
rooms = 0

for i in range(student_amount):
    S, Y = map(int,input().split())
    if S == 1:
        boy[Y-1] += 1
    else:
        girl[Y-1] += 1

for i in range(6):
    rooms += boy[i] // room_limit
    if boy[i] % room_limit != 0:
        rooms += 1
    rooms += girl[i] // room_limit
    if girl[i] % room_limit != 0:
        rooms += 1

print(rooms)