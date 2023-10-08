A, B = map(int,input().split())
ans = 1000
def AtoB(a,b,cnt):
    global ans
    if a > b:
        return
    if a == b:
        if ans > cnt:
            ans = cnt
        return
    else:
        AtoB(a*2,b,cnt+1)
        a = str(a) + '1'
        AtoB(int(a),b,cnt+1)
AtoB(A,B,0)
if ans == 1000:
    print(-1)
else:
    print(ans+1)