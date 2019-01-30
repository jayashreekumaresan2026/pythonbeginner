elements = int(input("Enter the value"))


def global_block():
    for num1 in range(1, elements + 1):
        for inum2 in range(1, num1 + 1):
            print("*", end="  ")
        print()


def local_block():
    for num1 in range(elements + 1, 1, -1):
        for num2 in range(1, num1 - 1):
            print("*", end=" ")
        print()


global_block()
local_block()
