import sys
#from collections import deque

test_case=int(sys.stdin.readline())
for _ in range(test_case):
    AC = sys.stdin.readline()
    N = int(sys.stdin.readline())
    nums_input = sys.stdin.readline()
    if N == 0:
        nums = []
    else:
        nums = list(map(int,nums_input[1:-2].split(',')))

    s = True
    for func in AC:
        if func == 'R':
            nums = nums[::-1]
        elif func == 'D':
            if nums:
                nums.pop(0)
            else:
                s = False
                break

    if s == True:
        print(nums)
    else:
        print('error')