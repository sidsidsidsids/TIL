#
# import sys
# S = sys.stdin.readline().strip()
# S_l = len(S)
# idx = 0
# able = True
# while idx < S_l:
#     if S[idx] == 'p':
#         if idx+1 < S_l and S[idx+1] == 'i':
#             idx += 2
#         else:
#             able = False
#             break
#     elif S[idx] == 'k':
#         if idx+1 < S_l and S[idx+1] == 'a':
#             idx += 2
#         else:
#             able = False
#             break
#     elif S[idx] == 'c':
#         if idx+1 < S_l and S[idx+1] == 'h':
#             if idx+2 < S_l and S[idx+2] == 'u':
#                 idx += 3
#         else:
#             able = False
#             break
#     else:
#         able = False
#         break
#
# if able:
#     print('YES')
# else:
#     print('NO')


import re

check = re.compile('(pi|ka|chu)*')
S = input()

if re.fullmatch(check, S) :
    print("YES")
else:
    print("NO")