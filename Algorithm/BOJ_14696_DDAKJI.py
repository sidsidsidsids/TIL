test_cases = int(input())
for tc in range(test_cases):
    A, *A_ddakji = map(int,input().split())
    B, *B_ddakji = map(int, input().split())
    if A_ddakji.count(4) > B_ddakji.count(4):
        print('A')
    elif A_ddakji.count(4) < B_ddakji.count(4):
        print('B')
    else:
        if A_ddakji.count(3) > B_ddakji.count(3):
            print('A')
        elif A_ddakji.count(3) < B_ddakji.count(3):
            print('B')
        else:
            if A_ddakji.count(2) > B_ddakji.count(2):
                print('A')
            elif A_ddakji.count(2) < B_ddakji.count(2):
                print('B')
            else:
                if A_ddakji.count(1) > B_ddakji.count(1):
                    print('A')
                elif A_ddakji.count(1) < B_ddakji.count(1):
                    print('B')
                else:
                    print('D')