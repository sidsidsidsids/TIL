def tree_LVR_with_cal(s):
    if s == 0 or (c1[s] == 0 and c2[s] == 0):
        return

    tree_LVR_with_cal(c1[s])

    if dictionary[c1[s]] not in ['*','+','/','-'] and dictionary[c2[s]] not in ['*','+','/','-']:
        if dictionary[s] == '*':
            b = int(dictionary[c2[s]])
            a = int(dictionary[c1[s]])
            dictionary[s] = a * b
            dictionary[c1[s]] = dictionary[c2[s]] = 0
        elif dictionary[s] == '/':
            b = int(dictionary[c2[s]])
            a = int(dictionary[c1[s]])
            dictionary[s] = a / b
            dictionary[c1[s]] = dictionary[c2[s]] = 0
        elif dictionary[s] == '+':
            b = int(dictionary[c2[s]])
            a = int(dictionary[c1[s]])
            dictionary[s] = a + b
            dictionary[c1[s]] = dictionary[c2[s]] = 0
        elif dictionary[s] == '-':
            b = int(dictionary[c2[s]])
            a = int(dictionary[c1[s]])
            dictionary[s] = a - b
            dictionary[c1[s]] = dictionary[c2[s]] = 0

    tree_LVR_with_cal(c2[s])

for tc in range(1,11):
    dictionary = {}
    V = int(input())
    c1 = [0] * (V + 1)
    c2 = [0] * (V + 1)

    for _ in range(V):
        num, val, *c = input().split()
        dictionary[int(num)] = val

        if len(c) > 1:
            c1[int(num)] = int(c[0])
            c2[int(num)] = int(c[1])

        elif len(c) == 1:
            c1[int(num)] = int(c[0])

        else:
            pass

    for _ in range(10):
        tree_LVR_with_cal(1)
        #print(dictionary)

    answer = int(dictionary[1])

    print(f'#{tc} {answer}')