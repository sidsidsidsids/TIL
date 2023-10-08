'''

'''
N = int(input())
num_list = list(map(int,input().split()))
student_list = []

for i in range(N):
    student_list.insert(i-num_list[i],i+1)
print(*student_list)