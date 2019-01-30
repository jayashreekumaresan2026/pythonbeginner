array =[]
num = int(input("Enter the number range"))
def find_maximum():
    for i in range(1, num+1):
        user_input = int(input("Enter the number"))
        array.append(user_input)
    array.sort()
    return array[num-1]
print(find_maximum())
