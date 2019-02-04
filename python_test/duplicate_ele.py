
def Remove(duplicate):
   my_array= []
   for num in duplicate:
    if num not in my_array:
        my_array.append(num)
   return  my_array


duplicate = [6,7,8,6,8]
print(Remove(duplicate))