num = int(input())
arr = [0] * (num+2)
arr[0] = 0
arr[1] = 1
for i in range(2,num+2):
    arr[i] = arr[i-2] + arr[i-1]
print(arr[num+1] % 10007)