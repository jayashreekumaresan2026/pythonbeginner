
def birthdayCakeCandles(array):
    maximum=array[0]
    count=0
    for i in range(0,len(array)):
        if array[i]>maximum:
            maximum=array[i]
    for i in range(0,len(array)):
        if max==array[i]:
            count+=1
    return count
print(birthdayCakeCandles())