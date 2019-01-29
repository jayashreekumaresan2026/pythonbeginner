row = (input("Enter the height of the pyramid"))
row = int(row)
for i in range(0, row + 1):
    for j in range(0, i + 1):
        print(" # ", end=" ")
        print("")
