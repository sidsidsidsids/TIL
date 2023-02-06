test_case = int(input())
test_cnt = 1

for _ in range(test_case):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    answer = 0

    for i in range(1<<n):
        part_sum = 0
        for j in range(n):
            if i & (1<<j):
                part_sum += numbers[j]
                if part_sum == 0:
                    answer = 1

    print(f'#{test_cnt} {answer}')
    test_cnt += 1