test_cases = int(input())
for tc in range(test_cases):
    str1 = str(input())
    str2 = str(input())
    count_dict = {}

    for alphabet in str1:
        count_dict[alphabet] = 0 # 알파벳을 키로 가지는 딕셔너리
    for alphabet in str2:
        if alphabet in count_dict.keys(): # 딕셔너리에 알파벳이 있다면
            count_dict[alphabet] += 1 # value값 1 증가
   print(f'#{tc+1} {max(count_dict.values())}')
