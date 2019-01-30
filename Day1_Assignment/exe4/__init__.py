user_input=input("enter the inputs you want")
def sum(number1=1,number2=2):
  if(user_input =='yes'):
    if(number1!=number2):
     return number1+number2
  else:
   print("get the value from default")

print(sum(3,2))

