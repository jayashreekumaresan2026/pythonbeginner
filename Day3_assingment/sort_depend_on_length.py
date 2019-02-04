def length_of_element(length):
    return length
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    a.append(b)
a.sort(key=length_of_element)
print(a)
print(print())


