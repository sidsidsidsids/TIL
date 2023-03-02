import sys
sys.stdin = open("input.txt", "r")
for _ in range(10):
    test_case = int(input())
    arrays = []
    # 가로
    maximum = 0
    for i in range(100):
        arrays.append(list(map(int,input().split())))
        if maximum < sum(arrays[i]):
            maximum = sum(arrays[i])
    garo_sum = maximum
    # 세로
    maximum = 0
    sero = []
    for j in range(100):
        for i in range(100):
            sero.append(arrays[i][j])
        if maximum < sum(sero):
            maximum = sum(sero)
        sero = []
    sero_sum = maximum
    # 대각선
    cross1 = []; cross2 = []
    for i in range(100):
        cross1.append(arrays[i][i])
        cross2.append(arrays[i][99-i])
    
    print(f'#{test_case} {max(garo_sum, sero_sum, sum(cross1), sum(cross2))}')
       
    
