count=1
def myfun(* args):
    for i in range(1,len(*args)):
        count+=1
        if(count==2):
            print("I am called with:2 parameters")
        elif(count==3):
            print("I am called with:3 parameters")
        else:
            print("I am called with:4 parameters")
myfun(2,3)
myfun(4,5,6)
myfun(6,7,8,9)

