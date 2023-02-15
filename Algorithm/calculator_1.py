for tc in range(1,11):
    length = input()
    inputs = input()

    n_value = []; opr = []
    number = 0

    for n in inputs:
        if n.isdecimal():
            n_value.append(n)
        else:
            opr.append(n)

    postfix = ''

    postfix += n_value[0]
    for i in range(len(opr)):
        postfix += n_value[i+1]
        postfix += opr[i]

    number += int(postfix[0])
    for num in postfix[1::2]:
        number += int(num)
    print(f'#{tc} {number}')


    # for n in inputs[0::2]:
    #     number += int(n)
    # print(f'#{tc} {number}')
