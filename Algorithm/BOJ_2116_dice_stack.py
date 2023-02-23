n = int(input())
dices = [ list(map(int,input().split())) for _ in range(n) ]
opposite = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

for v in range(6):
    max_num = 0


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


