sentence = input()
target = str(input())

while target in sentence:
    sentence = sentence.replace(target,'')

if sentence:
    print(sentence)
else:
    print('FRULA')