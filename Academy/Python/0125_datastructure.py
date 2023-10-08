#주어진 문자열에서 숫자 문자 기호가 각각 몇개인지를 판단하는 함수 작성해보세요
'''
def check(target_str):
    pass
    l_count=0;n_count=0;count=0
    for i in target_str:
        if i.isdecimal() == True:
            n_count += 1
        elif i.isalpha() == True:
            l_count += 1
        else :
            count += 1
    return print(f'문자 : {l_count}개, 숫자 : {n_count}개, 기호 : {count}개')

check('q!1')
'''
#문자 : 개, 숫자 : 개, 기호 : 개
'''
sample_list = [11, 22, 33, 56, 67]

# 주어진 리스트의 4번째 자리(index : 3)에 있는 항목을 제거하고 변수에 할당해주세요

print("original list: ", sample_list)
elem=sample_list.pop(3)
print("list after: ", sample_list)
print("elem: ", elem)

# sample_list의 가장 뒤에 77를 추가해보세요
sample_list.append(77)

# 할당해놓은 변수의 값을 sample_list의 2번 index에 추가해 보세요
sample_list.insert(2,elem)
print("add elem: ", sample_list)

my_tuple = (1, 2, 3, 4, 5, 6)
#주어진 튜플에서 4와 5를 새로운 튜플에 할당해보세요
new_tuple = my_tuple[3:-1]
print(new_tuple)


test_list = [1, 2, 3, 7, 4, 6, 5]
test_list.sort()
print(test_list)


scores = [('eng', 88), ('sci', 90), ('mth', 80)]
# 정렬
print(scores)
scores.sort(key=lambda x: x[1])
print(scores)
'''





# 십진수를 이진수로 나타내는 재귀 함수
'''
def d(n):
    if n//2 == 0:
        return str(n%2)
    return d(n//2) + str(n%2)
N = int(input())
print(d(N))
'''

# 입력받은 리스트들을 묶는 애너그램
'''
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
''.join(words)
print(words)
'''
