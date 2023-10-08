num = int(input())
answer = []
maxlen = 0
for i in range(1,num):
    tester = [num, i, num - i]
    while tester[-2] - tester[-1] >= 0:
        tester.append(tester[-2] - tester[-1])
    if len(tester) > maxlen:
        maxlen = len(tester)
        answer = tester
if num == 1:
    print(4)
    print(1, 1, 0, 1)
else:
    print(maxlen)
    print(*answer)

