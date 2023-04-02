def numbers(i,j,cnt,key):
    global ans
    if cnt == 7:
        ans.add(key)
        return
    for ni, nj in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
        if 0 <= ni < 4 and 0 <= nj < 4:
            numbers(ni,nj,cnt+1,key+grid[ni][nj])


t = int(input())
for tc in range(1,1+t):
    grid = [ list(input().split()) for _ in range(4) ]

    ans = set()
    number = ''

    for i in range(4):
        for j in range(4):
            numbers(i,j,0,number)

    print(f'#{tc} {len(ans)}')