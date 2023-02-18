test_case = int(input())
for tc in range(test_case):
    n = int(input())
    prices = list(map(int,input().split()))

    profit = 0; maximum = 0
    for i in range(n-1,-1,-1):
        if prices[i] > maximum:
            maximum = prices[i]
        profit += maximum - prices[i]
        
    print(f'#{tc+1} {profit}')