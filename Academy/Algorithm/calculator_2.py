tc = 1
for _ in range(10):
    len_infix = input()
    infix = input()
    stack = []
    result = ''

    # 변환할 식을 순회
    for token in infix:
        # 토큰이 피연산자인 경우
        if token.isdecimal():
            result += token

        # 토큰이 연산자인 경우
        else:
            # 스택이 비어있는 경우, 스택에 push
            if not stack: # if len(stack) == 0
                stack.append(token)

            else:
                # incoming 우선순위가 2인 경우
                if token == '*':
                    # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+':
                    # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                    while stack:
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    for token in result:
        if token.isdecimal():
            stack += token

        # 토큰이 연산자인 경우
        else:
            # 스택이 비어있는 경우, 스택에 push
            if not stack: # if len(stack) == 0
                stack.append(token)

            else:
                # incoming 우선순위가 2인 경우
                if token == '*':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n1)*int(n2))

                # incoming 우선순위가 1인 경우
                elif token == '+':
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n1) + int(n2))

    print(f'#{tc} {stack[0]}')
    tc += 1