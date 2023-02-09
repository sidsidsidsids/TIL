test_cases = int(input())
for tc in range(test_cases):
    zandon_list = [0] * 8
    N = int(input())
    while N != 0 :
        if N >= 50000:
            i = N // 50000
            zandon_list[0] += i
            N -= 50000*i
        elif N >= 10000:
            i = N // 10000
            zandon_list[1] += i
            N -= 10000*i
        elif N >= 5000:
            i = N // 5000
            zandon_list[2] += i
            N -= 5000*i
        elif N >= 1000:
            i = N // 1000
            zandon_list[3] += i
            N -= 1000*i
        elif N >= 500:
            i = N // 500
            zandon_list[4] += i
            N -= 500*i
        elif N >= 100:
            i = N // 100
            zandon_list[5] += i
            N -= 100*i
        elif N >= 50:
            i = N // 50
            zandon_list[6] += i
            N -= 50*i
        elif N >= 10:
            i = N // 10
            zandon_list[7] += i
            N -= 10*i
        else:
            pass
    print(f'#{tc+1}')
    print(*zandon_list)