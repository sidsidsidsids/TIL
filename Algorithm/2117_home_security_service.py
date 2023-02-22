test_case = int(input())
for tc in range(1,test_case+1):
    N, M = map(int,input().split())
    city = [ list(map(int,input().split())) for _ in range(N) ]