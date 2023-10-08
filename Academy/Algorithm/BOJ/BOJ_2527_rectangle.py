'''
직사각형 : 첫 사각형 오른쪽 y,x가 두번째의 왼쪽 y,x보다 클 때
선분 : 동일한 x좌표(y좌표) 존재
점 : 첫 사각형의 한쪽 y 혹은 x와 반대쪽 x와 y 값과 두번째의 양쪽 각각의 y,x가 같을 때
없음 : 걍 없을 때
'''

for _ in range(4):
    F_x, F_y, F_p, F_q, S_x, S_y, S_p, S_q = map(int,input().split())

    if (F_x == S_p and F_q == S_y) or (F_y == S_q and F_x == S_p) or\
            (F_p == S_x and F_q == S_y) or (F_y == S_q and F_p == S_x):
        print('c')
    elif F_p < S_x or F_q < S_y or S_p < F_x or S_q < F_y:
        print('d')
    elif F_p == S_x or S_p == F_x or F_q == S_y or S_q == F_y:
        print('b')
    else:
        print('a')




