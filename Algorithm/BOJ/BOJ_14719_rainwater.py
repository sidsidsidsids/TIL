H, M = map(int,input().split())
block = list(map(int,input().split()))

left = 1
right = M-2
l_max = block[0]
r_max = block[-1]
rain = 0

while left < right:
    if block[left] >= l_max:
        l_max = block[left]
    else:
        rain += l_max - block[left]

    if block[right] >= r_max:
        r_max = block[right]
    else:
        rain += r_max - block[right]

    left += 1
    right -= 1

print(rain)
