test_cases = int(input())
for tc in range(test_cases):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    total_score = 0

    for i in range(K):
        total_score += max(scores)
        scores.remove(max(scores))

    print(f'#{tc+1} {total_score}')
