L = int(input())
while L < 100 and 0 < L:
    num_list = list(map(int,input().split()))
    amount = int(input())
    if amount > 100 or amount < 0:
        break
    else:
        pass
    count = 0
    while count < amount :
        gender_num = list(map(int,input().split()))
        gender = int(gender_num[0]) ; num = int(gender_num[1])
        if num > L:
            break
        if gender == 1:
            for i in range(1,L):
                if num*i > L:
                    break
                if num_list[num*i-1] == 1:
                    num_list[num*i-1] = 0
                else:
                    num_list[num*i-1] = 1
            print(num_list)
        elif gender == 2:
            if num_list[num-1] == 1:
                num_list[num-1] = 0
            else:
                num_list[num-1] = 1
            for i in range(1,L):
                if num+i-1 > L-1 or num-i-1 < 0:
                    break
                if num_list[num+i-1] == 1 and num_list[num-i-1] == 1:
                    num_list[num+i-1] = 0
                    num_list[num-i-1] = 0
                elif num_list[num+i-1] == 0 and num_list[num-i-1] == 0:
                    num_list[num+i-1] = 1
                    num_list[num-i-1] = 1
                else:
                    break   
            print(num_list)
        else:
            break 
        count += 1
    for i in range(len(num_list)):     
        if (i+1) % 20 == 0:
            print(num_list[i], end="\n")
        else:
            print(num_list[i], end=" ")
    # answer = ''
    # for i in num_list:
    #     answer += str(i)
    # for i in range(0,len(num_list),20):
    #     print(' '.join(answer[i:i+20]),sep="\n")
    break