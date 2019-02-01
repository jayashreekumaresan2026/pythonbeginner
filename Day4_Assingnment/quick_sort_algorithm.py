def quickSort(array):

  quickSorts(array,0,len(array)-1)

def quickSorts(array,low,high):

  if low<high:
      midpoint= partition(array,low,high)
      quickSorts(array,low,midpoint-1)
      quickSorts(array,midpoint+1,high)

def partition(array,low,high):

  pivotvalue = array[low]
  left = low+1
  right = high
  flag=0

  while flag!=0:
      while left<= right and array[left] <= pivotvalue:
          left= left + 1

      while array[right] >= pivotvalue and right >= left:
          right= right -1

      if right < left:
          flag=1
          temp = array[left]
          array[left] = array[right]
          array[right] = temp
      else:
          temp = pivotvalue
          pivotvalue= array[low]
          array[low] = temp

  return right

array = [54,26,93,17,77,31,44,55,20]
quickSort(array)
print(array)
