test_case = int(input())
for tc in range(test_case):
    prices = map(int,input().split())
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[i] < prices[j]