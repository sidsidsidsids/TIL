test_case = int(input())
for tc in range(test_case):
    word = str(input())
    if word == word[::-1]:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc + 1} 0')