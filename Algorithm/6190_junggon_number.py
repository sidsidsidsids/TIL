'''
test_cases = int(input())
for tc in range(test_cases):
    N = int(input())
    A = list(map(int,input().split()))
    danjo = []

    A_multiple = {}
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            A_multiple[A[i], A[j]]= (A[i]*A[j])

    #print(A_multiple)

    for num in A_multiple.values():
        if num < 10:
            danjo.append(num)
        else:
            #num = str(num)
            num_test = [0] * 9
            for i in range(8):
                num_test[i] += num // 10**(8-i)
            num_test[8] = num % 10
            d_check = 1
            for i in range(8):
                if num_test[i] <= num_test[i+1]:
                    continue
                else:
                    d_check = 0

            if d_check == 1:
                danjo.append(num)

    if len(danjo) == 0:
        print(f'#{tc+1} -1')
    else:
        danjo.sort()
        print(f'#{tc+1} {danjo[-1]}')

'''
test_cases = int(input())
for tc in range(1, test_cases + 1):
    N = int(input())
    nums = list(map(int,input().split()))
    AiAj = []

    for i in range(N-1):
        for j in range(i+1,N):
            AiAj.append(nums[i]*nums[j])

    AiAj.sort(reverse=True)
    answer = -1

    for num in AiAj:
        string_num = str(num)

        s = True
        for i in range(len(string_num)-1):
            if string_num[i] > string_num[i+1]:
                s = False
                break
            else:
                pass
        if s == True:
            answer = num
            break

    print(f'#{tc} {answer}')

        