a=[]
b=[]
c=a #c에 a의 주솟값을 준 것. (참조)

 
# print(id(a))
# print(id(b))
# print(id(c))

# result = (a is b)
# print(result) # False
# result = (a is c)
# print(result) # True
# result = (c is b)
# print(result) # False
 
# if not b :
#     print('b는 비어있습니다')
# 빈 리스트는 false, 0도 false
 
# result = True # 회원이 인증된 상태
 
# if not result:
#     print('인증을 해주세요')
 
 
# list
# boxes = ['a','B',['apple','banana','cherry']]
# print(len(boxes)) # 3
# print(boxes[2]) # ['apple','banana','cherry']
# print(boxes[2][-1]) # 'cherry'
# print(boxes[-1][1][0]) # b

# parameter = 함수에게 전달해주는 값 (input)
# print(list(range(1,10,2))) 

# 역순
# print(list(range(6,0,-1)))

# 슬라이싱
# print([1,2,3,4][0:4:2])
# print((1,2,3,4,5,)[0:4:2])
# print('abcdefg'[1:4:2])
# a[시작:] => 특정 인덱스부터 끝까지 가져오기
# a[:끝] => 시작부터 특정 위치까지 가져오기

# dict_a={'a':'apple','b':'banana'}
# result = dict_a.get('c') # 매칭되는 key 값이 없기 때문에 none을 반환한다.
# if not result :
#     print('no value')

# s='문자열입니다.'
# print(id(s))
# s='이것도?'
# print(id(s))

# num = 10
# print(id(num))
# num = 14
# print(id(num))
