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
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
    def push(self,x):
        self.stack.append(x)
    def __repr__(self):
        return self.stack
'''
'''
import sys

N = int(sys.stdin.readline())
count = 0
stack = []
while count < N:
    order = list(sys.stdin.readline().split())
    if len(order) == 1:
        if order[0] == 'pop':
            try:
                print(stack[-1])
                stack.pop()
            except:
                print(-1)
        elif order[0] == 'size':
            print(len(stack))
        elif order[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else :
                print(0)
        elif order[0] == 'top':
            if len(stack) > 0:
                print(stack[-1])
            else:
                print(-1)
        else:
            pass
    elif len(order) == 2:
        stack.append(order[1])
    else:
        pass
    count += 1
'''
'''
linked_list = '1->2->3->2->1'
as_list = linked_list.split('->')

def Palindrome(input_list):
    half = len(input_list)//2
    return input_list[:half] == input_list[::-1][:half]

print(Palindrome(as_list))
'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(3)
node1.next = node2
head = node1

print(node1.next.data)
print(node2.next)