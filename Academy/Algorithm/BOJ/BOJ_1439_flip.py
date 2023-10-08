n = input()

block_0 = 0
block_1 = 0

l = len(n)
i = 0

while i < l:
    if n[i] == '0':
        k = 0
        while n[i + k] == '0':
            k += 1
            if i+k >= l:
                break
        block_0 += 1
        i += k
    else:
        k = 0
        while n[i + k] == '1':
            k += 1
            if i+k >= l:
                break
        block_1 += 1
        i += k

print(min(block_0, block_1))