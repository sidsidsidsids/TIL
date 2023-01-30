count = 0
while count < 10 :
    N = int(input())
    buildings = list(map(int,input().split()))
    jomang = 0
    for i in range(2,N-2):
        others = [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]
        if buildings[i] > max(others):
            jomang += buildings[i] - max(others)
    print(f'#{count+1} {jomang}')
    count += 1
