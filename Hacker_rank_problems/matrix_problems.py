a = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]
print(len(a))
for i in range(0, len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()
