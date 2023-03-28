t = int(input())
for test_case in range(1,t+1):
    board, change = input().split()
    change = int(change)
    b_list = []
    for n in board:
        b_list.append(int(n))

    maxima = max(b_list)
    test_list = list()
    for n in b_list:
        if n != maxima:
            test_list.append(n)
    secondmax = max(test_list)
    minima = min(b_list)
    lenlist = len(b_list)

    result = 0
    pp = [0] * lenlist
    def bonus(i,c):
        global result

        if i == c:
            ans = 0
            for p in range(lenlist):
                ans += b_list[lenlist-1-p] * 10**p
            if result < ans:
                result = ans
            return
        else:
            for j in range(lenlist-1):
                for k in range(j+1,lenlist):
                    b_list[j], b_list[k] = b_list[k], b_list[j]
                    if lenlist == 2:
                        bonus(i+1,c)
                    else:
                        if c >= 2 and b_list[0] == maxima:
                            if i <= 1 or (i >= 2 and b_list[-1] == minima) or i >= change-4:
                                bonus(i+1,c)
                        elif c <= 1:
                            bonus(i+1,c)
                        b_list[j], b_list[k] = b_list[k], b_list[j]
    bonus(0, change)
    print(f"#{test_case} {result}")
