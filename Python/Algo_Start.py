'''
a = 10
c = 7
b = '0b1010'
print(f'{a:b}')
print(f'{c:b}')
print(f'{a:08b}') # 자릿수 고정
print(bin(a))
print(int(b,2)) # int(x,2) : 이진수임을 알려줌
'''

'''
test_case = int(input())
for tc in range(1, test_case+1):
    # 01D06079861D79F99F
    arr = input()
    bin_scale = ''
    for x in arr:
        num = int(x,16)
        for j in range(3, -1, -1):
            bit = 1 if num&(1<<j) else 0
            bin_scale += str(bit)
    #print(bin_scale)

    # 000000011110000001100000011110011000011000011101011110011111100110011111
    arr_2 = [0] * len(bin_scale)
    for n in range(len(bin_scale)):
        arr_2[n] = bin_scale[n]
    N = len(arr_2)
    num_2 = 0
    last = []
    last_num = ''

    for i in range(N):
        k = i % 7
        num_2 += int(arr_2[i]) * (2**(6-k))
        if k == 6: # 7개 끊기
            print(num_2, end=' ')
            num_2 = 0

        if N+1 - i < 4:
            last = arr_2[i:]
            for j in range(len(last)):
                last_num += last[j]
            print(int(last_num,2), end=' ')
            break
    print()
'''
a = [3,5,6]
print(4 not in a)
