test_case = int(input())
for tc in range(test_case):
    '''
    sentence = input()
    num = ''; opr = ''
    answer = ''

    for w in sentence:
        if w.isdigit():
            num += w
        else:
            opr += w

    for n in num:
        answer += n
    for o in opr[::-1]:
        answer += o

    print(f'#{tc+1} {answer}')
    
    '''
    # extra
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
            if not stack:  # if len(stack) == 0
                stack.append(token)

            else:
                # (는 incoming 우선순위가 가장 높음
                if token == '(':
                    stack.append(token)
                # )는 (가 나올때까지 스택에서 pop, result에 append
                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()

                # incoming 우선순위가 2인 경우
                elif token == '*' or token == '/':
                    # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                    while stack and (stack[-1] == '*' or stack[-1] == '/'):
                        result += stack.pop()
                    stack.append(token)

                # incoming 우선순위가 1인 경우
                elif token == '+' or token == '-':
                    # 스택의 top 토큰이 우선순위가 낮을 때까지 스택에서 pop, result append
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    print(f'#{tc+1} {result}')

    # 피연산자
    # 스택에 push
    # 연산자 (*, / 연산 순서 주의
    # 스택에 담겨있는 2개의 토큰을 pop 후 연산 후 스택에 push='-') and (w == '*' or w == '/')