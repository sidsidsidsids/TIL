'''
def cases(array, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(array)):
        element = array[i]
        for rest in cases(array[i+1:], n-1):
            result.append([element] + rest)
    return result

tall = []
for _ in range(9):
    tall.append(int(input()))

seven_list = cases(tall, 7)
for lists in seven_list:
    if sum(lists) == 100:
        lists = sorted(lists)
        for num in lists:
            print(num)
        break
'''
# 합이 key인 부분집합의 수 구하기

tall = []
for _ in range(9):
    tall.append(int(input()))
tall.sort()

fake = sum(tall) - 100
s = 0

for a in range(8):
    if s == 1:
        break
    for b in range(a+1,9):
        if tall[a] + tall[b] == fake:
            a_t = tall[a]; b_t = tall[b]
            tall.remove(a_t); tall.remove(b_t)
            s = 1
            break

for n in tall:
    print(n)
