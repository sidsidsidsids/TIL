'''
입력값 : 테스트 케이스 수 , 숫자열 길이 , 숫자열
출력값 : 오름차순 내림차순 번갈아 반복하는 수열
'''
test_case = int(input())
for tc in range(test_case):
    N = int(input())
    numbers = list(map(int,input().split()))

    # sort
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    reversing_numbers = numbers[::-1]

    answer_sort = []; idx = 0

    while len(answer_sort) < 10:
        answer_sort.append(reversing_numbers[idx])
        answer_sort.append(numbers[idx])
        idx += 1

    print(f'#{tc+1}', *answer_sort)

