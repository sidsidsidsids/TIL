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

binary = '10110'
triple = '2101'
octal8 = '73'
sixten = 'A3'

print(int(binary,2))
print(int(triple,3))
print(int(octal8,8))
print(int(sixten,16))

target = '0F97A3'
target_bin = ''
for t in target:
    ten = int(t,16)
    binary_t = str(bin(ten))[2:]
    b_l = len(binary_t)
    if b_l == 3:
        binary_t = '0' + binary_t
    elif b_l == 2:
        binary_t = '00' + binary_t
    elif b_l == 1:
        binary_t = '000' + binary_t
    elif b_l == 0:
        binary_t = '0000'
    print(t, binary_t)
    target_bin += binary_t
answer = ''
for i in range(0,len(target_bin),7):
    target_ten = target_bin[i:i+7]
    output = str(int(target_ten, 2))
    answer = answer + output + ' '
print(answer)
