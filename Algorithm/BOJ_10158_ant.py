garo, sero = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

garo_t = t - (garo - p)
p = garo_t % garo

sero_t = t - (sero - q)
q = sero_t % sero

# a = 1; b = 1
# while t > 0:
#     p += a; q += b
#     if p == garo or p == 0:
#         a = -a
#     if q == sero or q == 0:
#         b = -b
#     t -= 1
print(p, q)