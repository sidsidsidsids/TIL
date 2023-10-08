n = int(input())
tree = [0] + [ [] for _ in range(n)]
c1 = [0] * (n+1)
c2 = [0] * (n+1)

for i in range(1,n+1):
    m, lc, rc = map(str,input().split())
    if lc != '.':
        c1[i] = lc
    if rc != '.':
        c2[i] = rc
    tree[i] = m

def VLR(s):
    if s:
        print(tree[s],end='')
        VLR(tree.index(c1[s]))
        VLR(tree.index(c2[s]))

def LVR(s):
    if s:
        LVR(tree.index(c1[s]))
        print(tree[s],end='')
        LVR(tree.index(c2[s]))

def LRV(s):
    if s:
        LRV(tree.index(c1[s]))
        LRV(tree.index(c2[s]))
        print(tree[s],end='')

VLR(1)
print()
LVR(1)
print()
LRV(1)


