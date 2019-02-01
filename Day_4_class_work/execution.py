my_array=[]
def sorting():
    value=int(input("enter the range"))
    for i in range(1,value):
      user_input=int(input("enter the values"))
      my_array.append(user_input)
      my_array.sort()
    return my_array
print(sorting())






