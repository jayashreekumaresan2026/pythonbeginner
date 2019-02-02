# my_list = ['p', 'q']
# n = 5
# new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in my_list]
# print(new_list)


my_list= []


value = int(input("enter the range "))
input("enter the character")
for k in range(1, value):
    my_list = str(input())


def my_lists(my_list,value):
    my_array=[]
    my_list =[]
    for i in  my_list:
        for j in range(1, value + 1):
            my_array.append("{}{}".format(i + j))
    return my_array


print(my_lists(my_list,value))
