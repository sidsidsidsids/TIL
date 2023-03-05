N = int(input())
words = [ [] for _ in range(N) ]
for i in range(N):
    word = input()
    if word in words:
        pass
    else:
        words[i] = word

words.sort(key=lambda X:[len(X), X])

for i in range(len(words)):
    if words[i] == []:
        pass
    else:
        print(words[i])
