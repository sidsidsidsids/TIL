class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1 # 포인트 클래스 인스턴스
        self.p2 = p2
        self.width = abs(self.p1.x - self.p2.x)
        self.height = abs(self.p1.y - self.p2.y)
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (self.width + self.height) * 2
    def is_square(self):
        return self.width == self.height


# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True
'''

class Stack:
    def __init__(self):
        self.stack = []
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
        # if self.stack:
              return self.stack[-1]
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
        # if not self.empty():
              return self.stasck.pop()
    def push(self,x):
        self.stack.append(x)
    def __repr__(self): # 객체 자체가 Return하는 것
        return self.stack

q = Stack()
print(q.top()) # None
q.push(2)
q.push(3)
print(q.top()) # 3
print(q.__repr__()) # [2,3]
print(q.empty()) # False
print(q.pop()) # 3
print(q.pop()) # 2
print(q.pop()) # None
print(q.__repr__()) # []
print(q.empty()) # True
q.push(6)
print(q.empty()) # False
print(q.top()) # 6
'''