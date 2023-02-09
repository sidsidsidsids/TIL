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