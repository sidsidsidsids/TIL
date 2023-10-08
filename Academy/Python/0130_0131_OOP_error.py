'''
# 고기 클래스를 정의하고 4개의 인스턴스를 만들어보자
class Meat:
    category = '정육'
    def __str__(self):
        print(f'{self.bread} 의 {self.part}는 한 근에 {self.price}이고 현재 {self.gram}만큼 남았습니다.')
    def __init__(self, bread, part, price, gram):
        self.bread=bread
        self.part=part
        self.price=price
        self.gram=gram
    # 인스턴스 함수
    def sold(self, s_gram): # s_gram 은 판매량
        print(f'{self.part}이(가) {s_gram}만큼 팔렸습니다.')
        self.gram -= s_gram
        print(f'{self.part}이(가) {self.gram}만큼 남았습니다.')


pork_belly = Meat('돼지','삼겹살','12000',600)

print(pork_belly.price)
print(Meat.category)
print(pork_belly)

pork_belly.sold(100)

def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕 {name}')

@emoji_decorator
def en_hello(name):
    print(f'hello {name}')
    
def add_emoji(name, func):
    func(name)
    print('^~^//')


en_hello('aiden')
# new_func = emoji_decorator(ko_hello)
# new_func('k')
# emoji_decorator(en_hello)('kk')
'''

class MyClass:
    def method(self):
        return 'instsance method', self

    @classmethod
    def classmethod(cls):
        return 'class method', cls

    @staticmethod
    def staticmethod():
        return 'static method'

# my_class = MyClass()
# print(my_class.method())
# print(my_class.classmethod())
# print(my_class.staticmethod())

# class Person:
#     def __init__(self):
#         self._age = 0
#     def get_age(self):
#         print('getter')
#         return self._age
#     def set_age(self, age):
#         print('setter')
#         self._age = age

#     age = property(get_age, set_age)

# p1 = Person()

# p1._age = 25 protected 지만 에러가 나지 않음
# print(p1._age) protected 지만 에러가 나지 않음

# p1.set_age(25)
# print(p1.get_age()) getter와 setter를 사용, 불편함

# age = property(get_age, set_age) 를 추가하여 자동으로 getter, setter

class Person:
    def __init__(self):
        self._age = 0
    @property
    def age(self):
        print('getter')
        return self._age
    @age.setter
    def age(self, age):
        print('setter')
        self._age = age

# p1 = Person()
# p1.age = 25
# print(p1.age) 

# 문자메시지 서비스를 구축할 때의 모델링
# sms : 1. 수신자, 발신자, 내용
class SMS:
    def __init__(self, receiver, sender, contents):
        self.receiver = receiver
        self.sender = sender
        self.contents = contents

    def __str__(self):
        return f'SMS 수신자 : {self.receiver}, 발신자 : {self.sender}, 내용 : {self.contents}'

    def send(self):
        return f'SMS 가 발송되었습니다.'

class LMS(SMS): # 자식 클래스
    def __init__(self, receiver, sender, contents):
        super().__init__(receiver, sender, contents)

    def __str__(self): # 재정의
        return f'LMS 수신자 : {self.receiver}, 발신자 : {self.sender}, 내용 : {self.contents}'

    def send(self):
        return f'LMS 가 발송되었습니다.'
        
s1 = SMS('01011241412','01010101010','short message')
print(s1)

l1 = LMS('01011241412','01010101010','long message')
print(l1)
print(l1.send())