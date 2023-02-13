test_cases = int(input())
for tc in range(test_cases):
    N = int(input())
    A = list(map(int,input().split()))
    danjo = []

    A_multiple = {}
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            A_multiple[A[i], A[j]]= (A[i]*A[j])

    print(A_multiple)

    for keys, num in A_multiple.items():
        if num < 10:
            danjo.append(num)
        else:
            num = str(num)
            d_check = 1
            for i in range(len(num)-1):
                if num[i] <= num[i+1]:
                    continue
                else:
                    d_check = 0

            if d_check == 1:
                danjo.append(int(num))

    if len(danjo) == 0:
        print(f'#{tc+1} -1')
    else:
        danjo.sort()
        print(f'#{tc+1} {danjo[-1]}')

