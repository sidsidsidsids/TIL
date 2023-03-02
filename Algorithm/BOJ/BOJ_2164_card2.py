import sys

N = int(sys.stdin.readline())
card = [0] * N
for i in range(N):
    card[i] = N-i

while len(card) > 1:
    card.pop()
    if len(card) > 1:
        top = card.pop()
        card.insert(0,top)

print(card[0])
