

for tc in range(1,11):
    N = int(input())
    infix = input()

    postfix = ''
    stack = []

    for token in infix:
        if token.isdecimal():
            postfix += token
        else:
            if not stack:
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            elif token == '*':
                while stack and stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(token)
            else:
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(token)
    
    for num in postfix:
        if num.isdecimal():
            stack.append(int(num))
        else:
            if num == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1*num2)
            elif num == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1+num2)
    
    print(f'#{tc} {stack[0]}')
