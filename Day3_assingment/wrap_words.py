def wrap_words():
     my_array=[]
     list_array=input("enter the element to be present")
     for i in  range(1,len(list_array)+1):
        my_array.append("{}".format(list_array[2:]+list_array[0:]))
     return my_array
print(wrap_words())
