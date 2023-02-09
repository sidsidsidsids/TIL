test_cases = int(input())
for tc in range(test_cases):
    str1 = str(input())
    str2 = str(input())
    count_dict = {}
    for alphabet in str1:
        count_dict[alphabet] = 0
    for alphabet in str2:
        if alphabet in count_dict.keys():
            count_dict[alphabet] += 1
    print(f'#{tc+1} {max(count_dict.values())}')
