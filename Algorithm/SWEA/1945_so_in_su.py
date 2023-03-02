total_cases=int(input())
case = 0
while case < total_cases:
    N = int(input())
    a = b = c = d = e = 0
    while N != 1 :
        if N % 11 == 0:
            e += 1
            N /= 11
        elif N % 7 == 0:
            d += 1
            N /= 7
        elif N % 5 == 0:
            c += 1
            N /= 5
        elif N % 3 == 0:
            b += 1
            N /= 3
        elif N % 2 == 0:
            a += 1
            N /= 2
        else:
            break
    print(f'#{case+1} {a} {b} {c} {d} {e}')
    case += 1
