test_case = int(input())
for tc in range(test_case):
    n = int(input())
    prices = list(map(int,input().split()))

    profit = 0
    for i in range(n-1):
        if prices[i] < max(prices[i+1:]):
            profit += max(prices[i+1:]) - prices[i]

    print(f'#{tc+1} {profit}')