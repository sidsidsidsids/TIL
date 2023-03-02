'''
for _ in range(1,11):
    tc = int(input())
    n = list(map(int,input().split()))

    while n[-1] > 0:
        for i in range(1,6):
            temp = n[0]
            temp -= i
            del n[0]
            if temp <= 0:
                temp = 0
                n.append(temp)
                break
            else:
                n.append(temp)
    print(f'#{tc}', *n)
'''
'''
def enqueue(item):
    global rear

    rear = (rear+1) % len(n)
    n[rear] = item

def dequeue():
    global front

    front = (front + 1) % len(n)
    temper = n[front]

    return temper

def isFull():
    return (rear+1) % len(n) == front


def pw(lst):
    cnt = 0
    while True:
        for i in range(1, 6):  # 1부터 5까지
            lst[cnt] -= i
            if lst[cnt] <= 0:  # 0 이하 되면 반환
                lst[cnt] = 0
                return lst
            cnt = (cnt + 1) % 8  # 8개니까 나머지로 계속 돌림


for tc in range(1, 11):
    t = int(input())
    lst = list(map(int, input().split()))
    new_lst = pw(lst)
    pos = new_lst.index(0) + 1

    print(f'#{tc} ', end='')
    for i in range(8):
        print(new_lst[(pos + i) % 8], end=' ')
    print()
'''
#import sys
#sys.stdin = open('input.txt')

for _ in range(1,11):
    tc = int(input())
    data = list(map(int,input().split()))

    cnt = 1

    while data[-1] > 0:

        if cnt > 5:
            cnt = 1

        # 첫번째 위치한 숫자를 감소시킨 뒤 맨 뒤로 보내기
        data.append(data.pop(0) - cnt)
        cnt += 1

    # 데이터의 마지막 값은 0으로 고정
    data[-1] = 0