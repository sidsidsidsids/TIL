
test_case = int(input())
for tc in range(1, test_case+1):
    num_len, num = input().split()
    num = str(num)
    print(f'#{tc}', end=' ')
    for n in range(int(num_len)):
        num_16 = int(num[n],16)
        if len(bin(num_16)) > 5:
            print(bin(num_16)[2:], end='')
        elif len(bin(num_16)) == 5:
            print('0'+bin(num_16)[2:], end='')
        elif len(bin(num_16)) == 4:
            print('00' + bin(num_16)[2:], end='')
        else:
            print('000' + bin(num_16)[2:], end='')
    print()