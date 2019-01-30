array = []

def add_element(array):
    sum=0
    for i in array:
        sum += i
    return sum

print("The list of element get added:")
print(add_element([1, 2, 3, 4]))
