N = int(input())
arr = list(map(int,input().split()))
len_arr = set(arr)
M = int(input())
target_arr = list(map(int,input().split()))

dictionary={}

for i in len_arr:
    dictionary[i] = 0
for i in range(N):
    dictionary[arr[i]] += 1

answer = [0] * M
for i in range(M):
    for keys, values in dictionary.items():
        if target_arr[i] == keys:
            answer[i] = values
            break

print(*answer)