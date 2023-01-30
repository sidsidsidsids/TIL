count = 0
while count < 10 :
    N = int(input())
    boxes = list(map(int,input().split()))
    dump = 0
    while max(boxes) - min(boxes) > 1:
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        dump += 1
        print(boxes)
        if dump > 1000:
            break
    print(f'#{count+1} {dump}')
    count += 1
