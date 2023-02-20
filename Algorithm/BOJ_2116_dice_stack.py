dices = int(input())

abcdef = list(map(int,input().split()))

six_index = abcdef.index(6)
if six_index == 0 or six_index == 5:
    survive = [0,5]
elif six_index == 1 or six_index == 3:
    survive = [1,3]
elif six_index == 2 or six_index == 4:
    survive = [2,4]
else:
    pass

for i in range(dices-1):

