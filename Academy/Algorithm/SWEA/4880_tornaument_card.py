'''
1 < 2 < 3 < 1
승자 맞추기

def f(i, j):    # i~j번까지의 승자를 찾는 함수
    if i==j:    # 한 명만 남은 경우
        return i
    else:       # 두 명 이상인 경우 두 그룹의 승자를 찾차 최종 승자를 가림
        left = f(i, (i+j)//2)       # 왼쪽 그룹의 승자
        right = f((i+j)//2+1, j)    # 오른쪽 그룹의 승자
        return win(left, right)     # 두 그룹의 승자를 찾는 함수

한번 하고 다시 나눌 때 고려하기
'''
def RSP(a, b):
    if a == 1 and b == 2:
        return [b, 1]
    elif a == 1 and b == 3:
        return [a, 0]
    elif a == 2 and b == 1:
        return [a, 0]
    elif a == 2 and b == 3:
        return [b, 1]
    elif a == 3 and b == 1:
        return [b, 1]
    elif a == 3 and b == 2:
        return [a, 0]
    else:
        return [a, 0]


test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    cards = list(map(int,input().split()))

    half = (N + 1) // 2
    pre_cards = cards[:half]
    post_cards = cards[half:]

    player = [i for i in range(1,N+1)]
    pre_players = player[:half]
    post_players = player[half:]

    print(pre_cards, post_cards)
    print(pre_players, post_players)

    while len(pre_cards) > 1:
        answer = []
        del_list = []
        for c in range(1,len(pre_cards),2):
            answer.append(RSP(pre_cards[c-1], pre_cards[c])[0])
            del_list.append(c - RSP(pre_cards[c-1], pre_cards[c])[1])
        if len(pre_cards) % 2:
            answer.append(pre_cards[-1])

        print(pre_cards, pre_players, del_list)

        for dead in del_list:
            pre_players[dead] = 0
        while min(pre_players) == 0:
            del pre_players[pre_players.index(min(pre_players))]

        pre_cards = answer

    while len(post_cards) > 1:
        answer = []
        del_list = []
        for c in range(1,len(post_cards),2):
            answer.append(RSP(post_cards[c-1], post_cards[c])[0])
            del_list.append(c - RSP(post_cards[c-1], post_cards[c])[1])
        if len(post_cards) % 2:
            answer.append(post_cards[-1])

        print(post_cards, post_players, del_list)

        for dead in del_list:
            post_players[dead] = 0
        while min(post_players) == 0:
            del post_players[post_players.index(min(post_players))]

        post_cards = answer

    # while len(cards) > 1:
    #     answer = []
    #     del_list = []
    #     for c in range(1,len(cards),2):
    #         answer.append(RSP(cards[c-1], cards[c])[0])
    #         del_list.append(c - RSP(cards[c-1], cards[c])[1])
    #     if len(cards) % 2:
    #         answer.append(cards[-1])
    #
    #     print(cards, player, del_list)
    #
    #     for dead in del_list:
    #         player[dead] = 0
    #     while min(player) == 0:
    #         del player[player.index(min(player))]
    #
    #     cards = answer

    if RSP(pre_cards[0], post_cards[0])[1] == 0:
        print(f'#{tc} {pre_players[0]}')
    else:
        print(f'#{tc} {post_players[0]}')


    # print(f'#{tc} {player[0]}')