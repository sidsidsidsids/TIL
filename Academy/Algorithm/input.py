import sys

sys.stdin = open('input.txt')

T=int(input())

for t in range(1, T+1) :
    ###
    count = 0
    while count < 10:
        case_num=int(input())
        inputs = list(map(int,input().split()))
        squares = []
        for i in range(0,len(inputs),10):
            squares.append(inputs[i:i+10])
        garo = [0]*100 ; sero = [0]*100 ; cross_1 = [0] ; cross_2=[0]
        for i in range(100) :
            garo[i] = squares[i]
            sero[i] = [squares[i][j] for j in range(100)]
            cross_1 = [squares[i][i]]
            cross_2 = [squares[i][j] for j in reversed(range(100))]
        for i in range(100) :
            garo[i] = sum(garo[i])
            sero[i] = sum(sero[i])
        cross_1 = sum(cross_1)
        cross_2 = sum(cross_2)
        answer=[]
        answer.append(garo)
        answer.append(sero)
        answer.append(cross_1)
        answer.append(cross_2)
        print(f'# {count+1} {max(answer)}')
    count += 1
    ###
print(T)