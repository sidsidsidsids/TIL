def fibonacci(n):
    global cnt_0
    global cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

test_case = int(input())
for tc in range(1,test_case + 1):
    cnt_0 = 0
    cnt_1 = 0
    num = int(input())
    fibonacci(num)
    print(cnt_0, cnt_1)
