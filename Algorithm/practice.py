'''
def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)


for i in range(-5, 6):
    print("%3d = " % i, end='')  # %x : align output line
    Bbit_print(i)
'''

import heapq


def find_kth_smallest(lst, k):
    heap = lst[:]
    heapq.heapify(heap)
    print(heap)

    for i in range(k-1, len(lst)):
        if lst[i] > heap[0]:
            heapq.heappop(heap)
            print(heap)
            heapq.heappush(heap, lst[i])
            print(heap)
        else:
            continue

    return heap[0]


lst = [3, 5, 2, 8, 1]
k = 3

result = find_kth_smallest(lst, k)
print(result)  # 3

