for _ in range(10):
    tc = int(input())
    word = str(input())
    sentence = str(input())
    cnt = 0

    for i in range(len(sentence) - len(word) + 1):
        if sentence[i : i+len(word)] == word:
            cnt += 1

    print(f'#{tc} {cnt}')