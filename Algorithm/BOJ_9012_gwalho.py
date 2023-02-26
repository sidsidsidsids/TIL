test_case = int(input())
for tc in range(1,test_case+1):
    check = input()
    stack = []
    for g in check:
        if g=='(':
            stack.append(g)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(g)
    if stack:
        print('NO')
    else:
        print('YES')