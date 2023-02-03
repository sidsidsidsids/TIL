import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int,input()))
    cnt = 0; max = 0
    for i in range(len(numbers)):
        if numbers[i] == 1:
            cnt += 1
            if i == len(numbers)-1:
                if cnt > max:
                    max = cnt
        else :
            if cnt > max:
                max = cnt
            cnt = 0


#     N=int(input())
#     lst=list(map(int,input()))
#     ans=cnt=0
#     for i in range(N):
#         if lst[i] == 0:
#             cnt=0
#         else:
#             cnt += 1
#             if ans < cnt:
#                 ans = cnt

    print(f'#{test_case}', max)