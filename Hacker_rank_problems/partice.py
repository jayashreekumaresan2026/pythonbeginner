input_string = input("Enter family members separated by comma ")
family_list  = input_string.split(",")
print(family_list)
print("Printing all family member names")
for name in family_list:
    print(name)