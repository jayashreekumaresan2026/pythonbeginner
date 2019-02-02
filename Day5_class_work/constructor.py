class Person:
    def __init__(self,name,age):
            self.name=name
            self.age=age
    def  print_details(self):
        print("the details of the student",self.name,self.age)

    def personal_details(self,college):
        self.college=college
        print("hai i am from :",college)


p = Person()
p.personal_details("sathyabama")
s= Person('ovi',7)
s.print_details()
