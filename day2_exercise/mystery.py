def mystery(num):                           #num=12
    sum = 1                                 #upto  num=5 sum=2^(num^2)
    for i in range(1, num):                 #after num=6 sum=(5*num)*(5^2)
        if i < 6:                           #upto  num=9 sum=(5*num)*(5^2)
            for k in range(1, num):         #after num=10 sum=(5*num)*(5^4)*(3^1)
                sum *= 2                    #after num=11 sum=(5*num)*(5^4)*(3^2)
        else:
            if i < 10:
                sum *= 5
            else:
                sum *= 3
    print(sum)
    return sum


mystery(12)
