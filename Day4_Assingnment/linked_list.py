# def creating_sorting():
#     n=int(input("enter the value"))
#     my_array=[]
#     for k in range(1,n+1):
#        element=int(input())
#        my_array.append(element)
def creating_sorting(my_array):
    n=len(my_array)

    for i in range(1,n+1):
        for j in range(1,n-i-1):
            if my_array[i]>my_array[i+1]:
                temp=my_array[i]
                my_array[i]=my_array[i+1]
                my_array[i+1]=temp

my_array=['A','D','C','E']
creating_sorting(my_array)
print("sorted items")
for i in my_array:
    print("%d"%my_array[i])





