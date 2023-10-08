for tc in range(1,11):
    N, pw = input().split()
    N = int(N)

    pw_list = []
    for n in pw:
        pw_list.append(n)

    for i in range(N-1):
        for k in range(N):
            if -1<i-k and i+1+k<N and pw_list[i-k] == pw_list[i+1+k]:
                pw_list[i-k] = 'x'
                pw_list[i+1+k] = 'x'
            else:
                break
    
    print(f'#{tc}', end=' ')

    for i in pw_list:
        if i == 'x':
            del i
        else:
            print(i, end='')
    print()
        

