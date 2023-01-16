a=[]
b=[]
c=a #c에 a의 주솟값을 준 것. (참조)

'''
print(id(a))
print(id(b))
print(id(c))

result = (a is b)
print(result) # False
result = (a is c)
print(result) # True
result = (c is b)
print(result) # False


if not b :
    print('b는 비어있습니다')
# 빈 리스트는 false, 0도 false

result = True # 회원이 인증된 상태

if not result:
    print('인증을 해주세요')
'''

#list
boxes = ['a','b',['apple','banana','cherry']]
print(len(boxes)) # 3
print(boxes[2]) # ['apple','banana','cherry']
print(boxes[2][-1]) # 'cherry'
print(boxes[-1][1][0]) # b
 