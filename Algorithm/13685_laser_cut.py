test_case = int(input())
for tc in range(1,test_case+1):
    stack = []
    values = input()

    cnt = 0
    ans = 0

    for i in range(len(values)):
        if values[i] == '(':
            cnt += 1
            stack.append(i)
        else: # values[i] == ')'
            if values[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    
    print(f'#{tc} {ans}')