import sys
count = 0
while count < 10 :
    Qnum = int(sys.stdin.readline())
    Square = list(map(int,sys.stdin.readline().split()))
    garo = []; sero = []; real_sero = []
    Square_sliced=[] ; cross_1 = 0 ; cross_2 = 0
    for i in range(0,10000,100):
        garo.append(Square[i:i+100])
    for i in range(len(garo)):
        garo[i] = sum(garo[i])
    for i in range(100):
        for j in range(100):
            sero.append(Square[i+j*100])
    for i in range(0, len(sero), 100):
        real_sero.append(sero[i:i+100])
    for i in range(len(real_sero)):
        real_sero[i] = sum(real_sero[i])
    for i in range(0, len(Square),100): 
        Square_sliced.append(Square[i:i+100])
    for i in range(100):
        cross_1 += Square_sliced[i][i]
        print(cross_1)
    for i in range(100):
        cross_2 += Square_sliced[i][99-i]
    maximum = max(max(garo), max(real_sero), cross_1, cross_2)
    print(f'#{count+1} {maximum}')
    count += 1