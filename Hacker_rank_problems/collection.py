import collections

array = []
b = 'a,b,c,d,a,c'
b = b.split(",")
print(b)
c = collections.Counter(b)
for i in c:
    if c[i] == 2:
        array.append(i)

print(array[0],array[1])
