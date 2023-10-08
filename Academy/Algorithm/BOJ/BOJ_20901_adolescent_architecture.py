import math

n = int(input())
cubes = []; cylns = []
arc = [[] for _ in range(n)]

for _ in range(n):
    shape, value = input().split()
    value = int(value)
    if shape == "cylinder":
        cylns.append(value)
    else:
        cubes.append(value)

cubes = sorted(cubes); cylns = sorted(cylns)
cubes_l = len(cubes); cylns_l = len(cylns)
cube_idx = 0; cyln_idx = 0

for idx in range(n):
    if cube_idx < cubes_l and cyln_idx < cylns_l:
        if cubes[cube_idx] / math.sqrt(2) <= cylns[cyln_idx]:
            arc[idx] = f'cube {cubes[cube_idx]}'
            cube_idx += 1
        elif cylns[cyln_idx] * 2 <= cubes[cube_idx]:
            arc[idx] = f'cylinder {cylns[cyln_idx]}'
            cyln_idx += 1
        else:
            arc = ['impossible']
            break
    else:
        if cube_idx < cubes_l:
            arc[idx] = f'cube {cubes[cube_idx]}'
            cube_idx += 1
        else:
            arc[idx] = f'cylinder {cylns[cyln_idx]}'
            cyln_idx += 1

for a in arc:
    print(a)

