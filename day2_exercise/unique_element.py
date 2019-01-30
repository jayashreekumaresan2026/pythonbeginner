str = input("enter the string ")
def char_frequency(str):
    for i in str:
        print("{}:{}".format(i,str.count(i)))


char_frequency(str)
