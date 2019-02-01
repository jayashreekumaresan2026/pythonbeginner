inputs=int(input("enter the value of range"))
def sorting():
    values = int(input("enter the values"))
    for i in range(1,values):
        for j in range(1, values):
            if(num_[i]>num_[j]):
                temp=num_[i]
                num_[j]=num_[j]
                num_[j]=temp
    return(num_[i])
print(sorting())


