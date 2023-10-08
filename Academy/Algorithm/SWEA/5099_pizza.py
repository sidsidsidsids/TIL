'''
7 2 6

3 1 3
1 0(5) 1
0(3) 2 0
1 1
0 0

'''
test_case = int(input())
for tc in range(1, test_case + 1):
    N, M = map(int,input().split())
    pizzas = list(map(int,input().split()))

    # 피자에 번호 넣어주기 : [번호, 치즈 양]을 원소로 가지는 리스트 선언
    pizza = []
    for i in range(M):
        pizza.append([i+1, pizzas[i]])

    # 오븐과 오븐에 있는 피자들의 번호를 저장할 리스트들 선언
    oven = [0] * N; number = [0] * N
    # 초기 셋팅 : 오븐에는 치즈 양을, 번호에는 피자 번호를 N개 받음
    for i in range(N):
        pizza_pop = pizza.pop(0)
        oven[i], number[i] = pizza_pop[1], pizza_pop[0]

    # 다 굽는 횟수를 셀 변수 선언
    cnt = 0
    # M-1번 구울 때 까지(피자를 하나 빼고 다 구울 때까지) 순회
    while cnt < M-1:
        # 오븐 크기만큼 순회
        for i in range(N):
            # 다 굽고 남은거 고려 X
            if oven[i] == 0:
                continue

            # 구워서 녹은 치즈
            oven[i] = oven[i] // 2
            # 남은 치즈가 0이 될 때 cnt +1
            if oven[i] == 0:
                cnt += 1
                # 하나 빼고 다 구우면 반복문 멈춤
                if cnt == M-1:
                    break
                else:
                    # 더 구워야 할 피자들이 있으면 피자 대체
                    if len(pizza) > 0:
                        pizza_pop = pizza.pop(0)
                        oven[i], number[i] = pizza_pop[1], pizza_pop[0]
                    else:
                        pass

    # 오븐에 남아있는 건 치즈가 남은 피자 1개와 그 외 치즈가 다 녹은 N-1개의 피자들
    # 녹은 거 다 제거
    while len(number) > 1:
        idx = oven.index(0)
        del oven[idx]
        del number[idx]

    print(f'#{tc} {number[0]}')




