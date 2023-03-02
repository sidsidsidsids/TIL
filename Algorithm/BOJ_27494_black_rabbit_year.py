n = int(input())
cnt = 0
for nu in range(1,n+1):
    if nu >= 2023:
        num = str(nu)
        for i in range(len(num)):
            if num[i] == '2':
                for j in range(i+1, len(num)):
                    if num[j] == '0':
                        for k in range(j+1, len(num)):
                            if num[k] == '2':
                                for l in range(k+1,len(num)):
                                    if num[l] == '3':
                                        cnt += 1
print(cnt)

