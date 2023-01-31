for _ in range(10) :
    Qnum = int(input())
    Square = []
    for _ in range(100):
        Square.append(list(map(int,input().split())))
    
    garo_max = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += Square[i][j]
        if sum > garo_max :
            garo_max = sum
    
    sero_max = 0
    for i in range(100) :
        sum = 0
        for j in range(100) :
            sum += Square[j][i]
        if sum > sero_max :
            sero_max = sum

    cross_max = 0
    for i in range(100) :
        sum1 = 0
        sum2 = 0
        sum1 += Square[i][i]
        sum2 += Square[i][99-1]
        if sum1 > sum2 :
            cross_max = sum1
        else :
            cross_max = sum2

    maximum = max(garo_max, sero_max, cross_max)
    print(f'#{Qnum} {maximum}')


    # garo = []; sero = []; real_sero = []
    # Square_sliced=[] ; cross_1 = 0 ; cross_2 = 0
    # for i in range(0,10000,100):
    #     garo.append(Square[i:i+100])
    # print(garo[2])
    # for i in range(len(garo)):
    #     garo[i] = sum(garo[i])
    # maximum = max(garo)
    # for i in range(100):
    #     for j in range(100):
    #         sero.append(Square[i+j*100])
    # for i in range(0, len(sero), 100):
    #     real_sero.append(sero[i:i+100])
    # for i in range(len(real_sero)):
    #     real_sero[i] = sum(real_sero[i])
    # if max(real_sero) > maximum:
    #     maximum = max(real_sero)
    # for i in range(0, len(Square),100): 
    #     Square_sliced.append(Square[i:i+100])
    # for i in range(100):
    #     cross_1 += Square_sliced[i][i]
    # if cross_1 > maximum:
    #     maximum = cross_1
    # for i in range(100):
    #     cross_2 += Square_sliced[i][99-i]
    # if cross_2 > maximum:
    #     maximum = cross_2
    # print(f'#{Qnum} {maximum}')