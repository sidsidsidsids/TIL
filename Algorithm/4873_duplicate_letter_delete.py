test_case = int(input())
for tc in range(test_case):
    sentence = list(map(str,input()))

    i = 0
    stack = []

    while i < len(sentence):
        stack.append(sentence[i])
        if len(stack) != 1 and stack[-2] == stack[-1]:
        # 기존에 있던 낱말과 새로 들어온 낱말이 같다면 둘다 제거
            stack.pop()
            stack.pop()

        i += 1

    print(f'#{tc+1} {len(stack)}')
