array = []
ranges = int(input("Enter the range of list"))
def add_element():
    for i in range(1,ranges):
        sum=0
        number = int(input("enter the number to be added"))
        array2= array.append(number)
        size_array=len(array2)
        for i in (1,size_array):
            sum +=i
    return sum
print(add_element())
