result = [[3,6],[1,3],[3,5]]
if result:
    result.sort(lambda X: (X[0], X[1]))
else:
    print(False)
print(result)