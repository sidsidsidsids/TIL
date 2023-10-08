# sentence = input()
# target = list(str(input()))
# while target in sentence:
#     sentence = sentence.replace(target,'')
# '''
# idxs를 돌면서
# 타겟일 경우 해당 타겟의 idx 전부 1 처리
# 그 다음 i를 target 길이만큼 앞으로 당기고 다시 순회
# 그 다음 타겟 판별 여부는 idxs에 1이 아닌 것들만 순회
# '''
# l_s = len(sentence)
# l_t = len(target)
# i = 0
# idxs = [0] * l_s
# tmp = [0] * l_t
#
# while i < l_s:
#     if sentence[i] == target[0]:
#         j = 0
#         j_c = 0
#         able = True
#         while j < l_t:
#             if i+j_c >= l_s or i >= l_s:
#                 able = False
#                 break
#             if idxs[i + j_c]:
#                 j_c += 1
#             else:
#                 if sentence[i+j_c] == target[j]:
#                     tmp[j] = i+j_c
#                     j += 1
#                     j_c += 1
#                 else:
#                     able = False
#                     break
#         if able:
#             for t in tmp:
#                 idxs[t] = 1
#             i -= l_t
#             if i < 0:
#                 i = 0
#         else:
#             i += 1
#     else:
#         i += 1
#
# if l_s != sum(idxs):
#     answer = ''
#     for k in range(l_s):
#         if not idxs[k]:
#             answer += sentence[k]
#     print(answer)
# else:
#     print('FRULA')


from collections import deque
sentence = input()
target = list(str(input()))

stack = list()

l_s = len(sentence)
l_t = len(target)

for s in sentence:
    stack.append(s)
    # print(stack[-1])
    if stack[-1] == target[-1]:
        if len(stack) >= l_t and stack[-l_t:] == target[-l_t:]:
            for _ in range(l_t):
                stack.pop()
answer = ''
if stack:
    for l in stack:
        answer += l
else:
    answer = 'FRULA'
print(answer)

