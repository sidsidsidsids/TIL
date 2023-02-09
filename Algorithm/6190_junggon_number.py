test_cases = int(input())
for tc in range(test_cases):
    N = int(input())
    A = list(map(int,input().split()))
    danjo = []
    for i in range(N):
        danjo_test = []
        for j in range(len(str(A[i]))):
            danjo_test.append(A[i]%10)
        if len(danjo_test) != 1:
            for j in range(len(danjo_test) - 1):
                if danjo_test[j] < danjo_test[j + 1]:
                    break
                else:
                    if j == len(danjo_test) - 2:
                        danjo.append(A[i])
        else:
            danjo.append(A[i])
    print(danjo)