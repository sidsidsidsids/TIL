test_case = int(input())
for tc in range(test_case):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')