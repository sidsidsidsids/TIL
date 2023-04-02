a=[[[1,2,3],[4,5,6]],[[3,25,3],[5,6,16]]]
b=[]
for i in range(len(a)):
    for j in range(len(a[i])):
        b.append(a[i][j])
print(b)