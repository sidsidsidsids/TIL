test_case = int(input())
for _ in range(test_case):
    n = int(input())
    cnt = 0
    for i in range(11):
        for j in range(6):
            for k in range(4):
                if i + 2*j + 3*k == n:

    print(cnt)