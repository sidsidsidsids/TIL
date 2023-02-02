total_case = int(input())
case = 0
while case < total_case:
    numbers = list(map(int,str(input())))
    num_count = [0]*(10+2)
    # 10 : 0~9까지의 수, +2 : triplet 판별 시 인덱스에러 방지(for i in range(10))
    for i in numbers:
        num_count[i] += 1
    run = 0 ; triplet = 0
    for i in range(10):
        if num_count[i] >= 3:
            num_count[i] -= 3
            triplet += 1
            if num_count[i] >= 3:
                num_count[i] -= 3
                triplet += 1
        if num_count[i] >= 1 and num_count[i+1] >= 1 and num_count[i+2] >= 1:
            num_count[i] -= 1
            num_count[i+1] -= 1
            num_count[i+2] -= 1
            run += 1
            if num_count[i] >= 1 and num_count[i + 1] >= 1 and num_count[i + 2] >= 1:
                num_count[i] -= 1
                num_count[i + 1] -= 1
                num_count[i + 2] -= 1
                run += 1
    if run + triplet == 2:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')
    case += 1
