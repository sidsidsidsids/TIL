test_cases = int(input())
for tc in range(test_cases):
    student_amount, c = map(int,input().split())
    student_list = [i+1 for i in range(student_amount)]
    student_complete = list(map(int,input().split()))
    for c in student_complete:
        student_list.remove(c)
    print(f'#{tc+1}', *student_list)

