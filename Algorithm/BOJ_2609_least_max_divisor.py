A, B = map(int,input().split())
if A > B:
    for n in range(B,0,-1):
        if A % n == 0 and B % n == 0:
            max_divisor = n
            break
    k = A
    while True:
        if k % A == 0 and k % B == 0:
            min_divisor = k
            break
        else:
            k += 1

else:
    for n in range(A,0,-1):
        if A % n == 0 and B % n == 0:
            max_divisor = n
            break
    k = B
    while True:
        if k % A == 0 and k % B == 0:
            min_divisor = k
            break
        else:
            k += 1

print(max_divisor)
print(min_divisor)
