n = int(input())
dices = [ list(map(int,input().split())) for _ in range(n) ]
opposite = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
max_sum = 0

for v in range(6):

    numbers = [0]*6
    for i in range(6):
        numbers[i] = dices[0][i]

    total = 0
    bot_idx = v
    top_idx = opposite[bot_idx]
    bot_v = numbers[bot_idx]
    top_v = numbers[top_idx]

    numbers.remove(bot_v)
    numbers.remove(top_v)

    total += max(numbers)

    for k in range(1,n):

        numbers = [0] * 6
        for i in range(6):
            numbers[i] = dices[k][i]

        n_bot_idx = numbers.index(top_v)
        n_top_idx = opposite[n_bot_idx]
        bot_v = numbers[n_bot_idx]
        top_v = numbers[n_top_idx]

        numbers.remove(bot_v)
        numbers.remove(top_v)

        total += max(numbers)

    if max_sum < total:
        max_sum = total

print(max_sum)


# a_list = []; b_list = []; c_list = []; d_list = []; e_list = []; f_list = []
# dice = []
# for _ in range(dices):
#     a, b, c, d, e, f = map(int,input().split())
#     a_list.append(a)
#     b_list.append(b)
#     c_list.append(c)
#     d_list.append(d)
#     e_list.append(e)
#     f_list.append(f)
#     dice.append([a,b,c,d,e,f])
#
# top = [0] * (dices - 1)
# bot = [0] * (dices - 1)
#
# for i in range(dices):
#     for k in dice[i]:
#         top[i] = k
#         if k == a_list[0]:
#             bot[i] = k


