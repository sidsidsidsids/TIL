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
'''
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
'''
def tree_dist(s):
    dist[s] += 1

tree = [1, 2, 3, 4, 5]
left = [2, 4, None, None, None]
right = [3, 5, None, None, None]
dist = [0]*(5+1)
'''
'''
def tree_convertor(s):
    if s and left[s] and right[s]:
        tree_val[left[s]], tree_val[right[s]] = tree_convertor(right[s]), tree_convertor(left[s])
        return tree_val[s]
    elif s:
        pass
    return None

tree_idx = [None, 1, 2, 3, 4, 5, 6, 7]
tree_val = [None, 4, 2, 7, 1, 3, 6, 9]
left = [None, 2, 4, 6, None, None, None, None]
right = [None, 3, 5, 7, None, None, None, None]

tree_convertor(1)
print(tree_val)


# tree = [3,9,20,null,null,15,7]
# n = 1
# while True:
#     if len(tree) < 2**n:
#         for i in range(2**(n-1),len(tree)):
#
#     n += 1
'''
'''
tree_idx = [None,1,2,3,4,5,6,7,None,None,None,11,None,None,None,15]
tree_val = [None,4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
left = [None,2,4,6,None,None,None,None,None,None,None,None,None,None,None,None]
right = [None,3,5,7,None,11,None,15,None,None,None,None,None,None,None,None]
path_total = 0

def tree_sum(s):
    global path_total
    if s:
        tree_sum(right[tree_idx[s]])
        if tree_val[s] != None:
            path_total += tree_val[s]
            tree_val[s] = path_total
        tree_sum(left[tree_idx[s]])

tree_sum(1)
print(tree_val)
'''
'''
tree_idx = [None,1,2,3,4,5,None,7]
tree_val = [None,10,5,15,3,7,None,18]
left = [None,2,4,None,None,None,None,None]
right = [None,3,5,7,None,None,None,None]
L = 7
R = 15
total = 0

def tree_sum_with_limit(s):
    global total
    if s:
        tree_sum_with_limit(right[tree_idx[s]])
        if L <= tree_val[s] <= R:
            total += tree_val[s]
        tree_sum_with_limit(left[tree_idx[s]])

tree_sum_with_limit(1)

print(total)
'''
'''
VLR_input = [3, 9, 20, 15, 7]
# 루트가 3, 루트의 왼쪽 자식이 9임을 알 수 있음
LVR_input = [9, 3, 15, 20, 7]
# 20이 9의 자식 노드가 아님을 알 수 있음
# 즉 20은 루트의 오른쪽 자식 노드이므로 
tree_idx = [1, 2, 3, 4, 5]
left = [2, ]
'''
'''
def binary_idx_search(array,target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        # mid = left+(right-left) // 2
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return 'not found'

nums = [-1,0,3,5,9,12]
target = 9
# nums.sort()
print(binary_idx_search(nums,target))

def intersection_of_two(A,B):
    intersection_group = []
    for a in A:
        if a in B:
            if a not in intersection_group:
                intersection_group.append(a)
            else:
                pass
        else:
            pass
    return intersection_group

def intersection_two_pointer(A,B):
    intersection_group = []
    A.sort(); B.sort()
    a_idx = 0; b_idx = 0
    while a_idx < len(A) and b_idx < len(B):
        if A[a_idx] > B[b_idx]:
            b_idx += 1
        elif A[a_idx] < B[b_idx]:
            a_idx += 1
        else:
            if A[a_idx] not in intersection_group:
                intersection_group.append(A[a_idx])
            a_idx += 1
            b_idx += 1
    return intersection_group

nums1 = [4,9,5]
nums2 = [9,4,8,9,4]
print(intersection_of_two(nums1,nums2))
print(intersection_two_pointer(nums1,nums2))

def searchMatrix(matrix, target):
    return any(target in row for row in matrix)

matrix = [ [1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30] ]
print(searchMatrix(matrix,5))
'''
'''
def single_num(inputlist):
    check = set(inputlist)
    for elem in check:
        if inputlist.count(elem) == 1:
            return elem

print(single_num([2,2,1,4,4]))

def HamDist(a,b):
    return bin(a^b).count('1')

print(HamDist(1,4))


def count_1(binary):
    cnt = 0
    for i in binary:
        if i == '1':
            cnt += 1
    return cnt

print(count_1('00000000000000000000000000001011'))
'''
'''
def sliding_window(L,k):
    left = 0
    right = k
    result = list()
    while right <= len(L):
        result.append(max(L[left:right]))
        left += 1
        right += 1
    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sliding_window(nums,k)) # [3, 3, 5, 5, 6, 7]

def longest_string(word, change):
    maxima = 0
    cnt = 0
    chance = 0
    chance += change

    for i in range(len(word) - 1):
        j = 1
        while True:
            if word[i] == word[i+j]:
                cnt += 1
                j += 1
                if i+j >= len(word):
                    if maxima < cnt+1:
                        maxima = cnt+1
                    break
            else:
                if chance:
                    chance -= 1
                    cnt += 1
                    j += 1
                    if i + j >= len(word):
                        if maxima < cnt+1:
                            maxima = cnt+1
                        break
                else:
                    if maxima < cnt + 1:
                        maxima = cnt + 1
                    chance += change
                    break
        if j == 0:
            break
        cnt = 0

    return maxima

s = "AAABBC"
k = 2
print(longest_string(s,k)) # 5

def cookie(children,cookies):
    children.sort()
    cookies.sort()

    i_idx = 0
    c_idx = 0

    possible = 0

    while c_idx < len(cookies):
        if children[i_idx] <= cookies[c_idx]:
            possible += 1
            c_idx += 1
            i_idx += 1
            if i_idx >= len(children):
                break
        else:
            c_idx += 1

    return possible

print(cookie([1,2,3],[1,1])) # 1
print(cookie([1,2],[1,2,3])) # 2
'''
import collections
def much_elem(elem_list):
    counts = collections.defaultdict(int)
    for elem in elem_list:
        if counts[elem] == 0:
            counts[elem] = elem_list.count(elem)

        if counts[elem] > len(elem_list) // 2:
            return elem

print(much_elem([3,2,3])) # 3
print(much_elem([2,2,1,1,1,2,2])) # 2

import numpy

def fibo(n):
    M = numpy.matrix([[0,1],[1,1]])
    print(M ** n)
    vec = numpy.array([[0],[1]])
    print(vec)
    print(numpy.matmul(M ** n, vec))
    return numpy.matmul(M ** n, vec)[0]

print(fibo(4)) # 3