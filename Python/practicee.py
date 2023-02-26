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
#8. linked list
linked_list = '1->2->3->2->1'
as_list = linked_list.split('->')

def Palindrome(input_list):
    half = len(input_list)//2
    return input_list[:half] == input_list[::-1][:half]

print(Palindrome(as_list))


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
'''
'''
def reversed_sum(a,b):
    a = a.split(' -> '); b = b.split(' -> ')
    a_val = 0; b_val = 0
    for i in range(len(a)):
        a_val += int(a[i]) * 10 ** (len(a)-(i+1))
    for i in range(len(b)):
        b_val += int(b[i]) * 10 ** (len(b)-(i+1))
    tot_val = a_val + b_val

    tot_val = str(tot_val)
    reversed_list = []
    for v in tot_val[::-1]:
        reversed_list.append(v)

    return(' -> '.join(reversed_list))

linked_list_1 = '2 -> 4 -> 3'
linked_list_2 = '5 -> 6 -> 4'

print(reversed_sum(linked_list_1, linked_list_2))

def node_pair_swap(L):
    L = L.split(' -> ')
    for i in range(0,len(L),2):
        L[i], L[i+1] = L[i+1], L[i]

    return(' -> '.join(L))

linked_list = '1 -> 2 -> 3 -> 4'
print(node_pair_swap(linked_list))
'''
'''
# 12. Graph
def f(i, k):
    if i == k:
        comb = []
        for j in range(k):
            if bit[j]:
                comb.append(nums[j])
        return ans.append(comb)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

nums = [1,2,3]
bit = [0]*len(nums)
ans=[]
f(0, len(nums))
print(ans)
'''
def pre_process(T):
    lps = [0] * len(T)

    # lps를 만들기 위한 prefix에 대한 idx,
    j = 0

    """
    i : pattern에서 지나가고 있는 id
    j : 지나가고 있는 idx와 pattern의 앞부분과 같은 부분에 대한 idx
    """

    # 처음부터 끝까지 순회를 돌면서
    for i in range(1, len(T)):
        # i 와 j가 같으면 lps의 i 자리에 j+1을 넣어줍니다.
        #(prefix idx 위치에 있는 char와 같으면 lps에 숫자 추가)
        if T[i] == T[j]:
            lps[i] = j + 1
            j += 1
        # 다르다면, j를 초기화 해주어 pattern의 가장 처음부터 인식하자.
        # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교.
        else:
            j = 0
            if T[i] == T[j]:
                lps[i] = j + 1
                j += 1

    return lps

T = 'abcdabeeababcdabcef'
P = 'eaba'

lps = pre_process(T)
print(lps)

