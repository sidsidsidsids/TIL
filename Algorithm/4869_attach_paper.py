'''
length > 3일때
홀수 : length-1 일 때 *2  +  length-3 일 때
짝수 : length-1 일 때 *2  -  length-3 일 때
'''

def cases(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        if n % 2: # 홀수면
            return cases(n - 1) * 2 - 1
        else:
            return cases(n - 1) * 2 + 1


test_case = int(input())
for tc in range(test_case):
    length = int(input())
    length_10 = int(length / 10)

    print(f'#{tc+1} {cases(length_10)}')