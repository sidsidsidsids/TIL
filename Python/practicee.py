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



def sum_f(candidates, target):
    result = []

    def dfs(goal, idx, status):
        if goal < 0:
            return
        if goal == 0:
            result.append(status)
            return
        for i in range(idx, len(candidates)):
            if candidates[i] == 0:
                continue
                # 0 예외 처리
            dfs(goal - candidates[i], i, status + [candidates[i]])
            # dfs 에서 i가 아닌 0을 넣으면 조합이 아닌 순열을 구현

    dfs(target, 0, [])
    return result

#print(sum_f(candidates=[0,2,3,6,7], target=7)) # [[2, 2, 3], [7]]

#
def bfs(start):
    Q = []
    time_total = 0
    visited[start] = 1
    Q.append(start)

    while Q:
        s = Q.pop(0)
        time_tmp = []
        for node in adjL[s]:
            if visited[node] == 0:
                visited[node] = 1
                Q.append(node)
                time_tmp.append(time(s,node))
        if time_tmp:
            time_total += max(time_tmp)

    return time_total

def time(from_n, to_n):
    for i in range(len(times)):
        if times[i][0] == from_n and times[i][1] == to_n:
            return times[i][2]
    else:
        return 0

times = [[2,1,1],[2,3,1],[3,4,1]] # [노드(from), 노드(to), 소요 시간]
N = 4 # 노드 개수
K = 2 # 출발 노드

L = len(times)
visited = [0] * (N+1)
adjL = [ [] for _ in range(N+1) ]

for i in range(L):
    adjL[times[i][0]] += [times[i][1]]

#print(bfs(K))
'''
tree = [3, 9, 20, None, None, 15, 7]

n = 1
while True:
    if len(tree) < 2**n:
        print(n)
        break
    n += 1
'''
def tree_dist(s):
    dist[s] += 1

tree = [1, 2, 3, 4, 5]
left = [2, 4, None, None, None]
right = [3, 5, None, None, None]
dist = [0]*(5+1)
'''
def tree_convertor(s):
    idx = tree.index(s)
    l_node = left[idx]
    r_node = right[idx]
    if l_node and r_node:
        l = tree.index(l_node)
        r = tree.index(r_node)
        tree[l], tree[r] = tree_convertor(r_node), tree_convertor(l_node)
        return s
    else:
        if idx%2:
            tree[idx-1], tree[idx] = tree[idx], tree[idx-1]

tree = [4, 2, 7, 1, 3, 6, 9]
left = [2, 1, 6, 0, 0, 0, 0]
right = [7, 3, 9, 0, 0, 0, 0]

tree_convertor(4)
print(tree)
'''

