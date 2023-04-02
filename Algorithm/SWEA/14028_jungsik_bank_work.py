'''
t = int(input())
for tc in range(1,1+t):
    binary = input()
    triple = input()

    s = 0
    for i in range(1,len(binary)):
        if s:
            break
        if binary[i]:
            binary[i] = '0'
        else:
            binary[i] = '1'
        for j in range(len(triple)):
            if j == 0:
                if triple[j] == 2:
                    triple[j] = 1
                else:
                    triple[j] = 2
            else:
                if triple[j]
'''


def func(b2, b3):
    for j in range(len(b2)):  # 이진수에서 바꿀 자리의 인덱스
        for c in range(2):  # 1이면 0으로 0이면 1로 바꾸기위해 반복문으로 0부터 1까지 꺼냄
            change_c = str(c)
            if change_c != b2[j]:  # 현재 바꾸려는 자리수와 c가 다르면
                new2 = b2[:j] + change_c + b2[j + 1:]  # 바꿔줌
        # print('new2: ',new2)

        for k in range(len(b3)):  # 3진수에서 바꿀 자리의 인덱스
            for l in range(3):  # 0이면 1 or 2로 / 1이면 0 or 2로 / 2면 0 or 1로 바꾸기위해 반복문으로 0부터 2까지 꺼냄
                n2 = int(new2, 2)  # 바꾼 2진수를 정수로 변환
                change_l = str(l)
                if change_l != b3[k]:  # 바꾸려는 자리의 숫자와 반복문에서 꺼낸 숫자가 다르면
                    new3 = b3[:k] + change_l + b3[k + 1:]  # 바꿔줌

                # print('new3: ',new3, end=' ')

                n3 = int(new3, 3)  # 3진수를 정수로 바꿔줌
                # print('n2: ',n2, 'n3: ',n3)
                if n2 == n3:  # 2진수와 3진수 변경한게 같으면
                    return n2  # 그 정수를 리턴


T = int(input())
for i in range(1, T + 1):
    b2 = input()
    b3 = input()

    print(f'#{i} {func(b2,b3)}')


