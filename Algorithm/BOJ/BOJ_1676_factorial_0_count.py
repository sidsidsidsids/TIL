number = int(input())
if number == 0:
    print(0)
else:
    fact = [0] * (number+1)
    fact[0] = 0
    fact[1] = 1
    for i in range(2,number+1):
        fact[i] = fact[i-1] * i
    checker = str(fact[number])

    cnt = 0
    for i in checker[::-1]:
        if i == '0':
            cnt += 1
        else:
            break

    print(cnt)