n = int(input())
members = [ [] for _ in range(n) ]
for i in range(n):
    age, name = input().split()
    members[i] += [int(age)]
    members[i] += [name]
members.sort(key=lambda x : x[0])

for i in range(len(members)):
    print(*members[i])