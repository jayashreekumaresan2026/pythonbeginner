def square_number_in_dictonary():
    elements=int(input("Enter the elements"))
    my_values_dic={i:i*i for i in range(1,elements+1)}
    print(my_values_dic)
square_number_in_dictonary()