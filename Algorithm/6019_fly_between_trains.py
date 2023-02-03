import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    D, A, B, F = map(int,input().split())
    time = D/(A+B)
    length = round(F*time,6)
    print(f'#{test_case} {length}')
