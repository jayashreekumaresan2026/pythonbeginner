fname = input("Enter file name:")
k = 0
# for line in fname:
#     words = line.split()
for i in fname:
    if (i.isspace()==True):
         k = k + 1
print("Occurrences of blank spaces:")
print(k)