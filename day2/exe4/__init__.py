user_input=input("enter the inputs you want")
def sum(a=1,b=2):
  if(user_input =='yes'):
    if(a!=b):
     return a+b
  else:
   print("get the value from default")

print(sum(3,2))

