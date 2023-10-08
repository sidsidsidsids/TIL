N, M = map(int,input().split())
dictionary = {}
for i in range(N):
    val = input()
    dictionary[i+1] = val
    dictionary[val] = i+1
for _ in range(M):
    question = input()
    if question.isdecimal():
        print(dictionary[int(question)])
    else:
        print(dictionary[question])