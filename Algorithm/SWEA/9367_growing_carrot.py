import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrots = list(map(int,input().split()))
    cnt = 0
    cnt_rec = []
    for i in range(1,len(carrots)):
        if carrots[i-1] < carrots[i]:
            cnt += 1
            if i == len(carrots)-1 :
                cnt_rec.append(cnt)
        else:
            cnt_rec.append(cnt)
            cnt = 0
    ans = max(cnt_rec) + 1
    print(f'#{test_case}', ans)