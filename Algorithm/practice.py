t=int(input())
length = int(input())
count = 0
while count < t:
    square = []
    f_ans=[0]*length; s_ans=[0]*length; t_ans=[0]*length
    for _ in range(length):
        square.append(input().split())
    for i in range(length):
        f_ans[i]=[square[j][i] for j in reversed(range(length))]
    for i in reversed(range(length)):
        s_ans[i]=[square[i][j] for j in reversed(range(length))]
        t_ans[i] = [square[j][i] for j in range(length)]
    for i in range(length):
        f_ans[i] = ''.join(f_ans[i])
        s_ans[i] = ''.join(s_ans[i])
        t_ans[i] = ''.join(t_ans[i])
    s_ans = s_ans[::-1] ; t_ans = t_ans[::-1]
    print(f'#{count+1}')
    for i in range(length):
        print(f_ans[i], s_ans[i], t_ans[i])  
    count += 1
