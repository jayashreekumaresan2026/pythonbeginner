# list with integer elements
list = [10, 20, 10, 30, 40, 10, 50]
# number (n) to be removed
n = 10

print ("Original list:")
print (list)

list.sort()
print(list)
for i in list:
	if(i==n):
		list.remove (i)

# print list after removing ODD elements
print ("list after removing ODD elements:")
print (list)

