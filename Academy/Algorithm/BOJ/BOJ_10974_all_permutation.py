def perm(i,k):
    if i == k:
        print(*p)
    else:
        for j in range(k):
            if used[j] == 0:
                p[i] = num_list[j]
                used[j] = 1
                perm(i+1, k)
                used[j] = 0

n = int(input())

num_list = []

for i in range(1,n+1):
    num_list.append(i)

p = [0]*n
used = [0]*n

perm(0,n)