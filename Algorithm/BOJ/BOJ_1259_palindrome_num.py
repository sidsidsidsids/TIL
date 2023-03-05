while True:
    number = input()
    if number == '0':
        break
    else:
        stringnum = str(number)
        if stringnum == stringnum[::-1]:
            print('yes')
        else:
            print('no')