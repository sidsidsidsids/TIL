n = int(input())
s = 0
if n == 1:
    print(1)
else:
    for i in range(n//2):
        if i**2 == n:
            print(1)
            break
    else:
        for i in range(n//2):
            if s == 2:
                break
            for j in range(n//2):
                if i**2 + j**2 == n:
                    s = 2
                    print(2)
                    break
        else:
            for i in range(n//2):
                if s == 3:
                    break
                for j in range(n//3):
                    if s == 3:
                        break
                    for k in range(n//4):
                        if i**2 + j**2 + k**2 == n:
                            s = 3
                            print(3)
                            break
            else:
                print(4)