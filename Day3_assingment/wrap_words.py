def wrap_words():
     my_array=[]
     list_array=input("enter the element to be present")
     for i in  range(1,len(list_array)+1):
        my_array.append("{}".format(list_array[i:]+list_array[0:i]))
     return my_array
print(wrap_words())
