class Person:
    def get_details(self):
        self.firstname = str(input("first"))
        self.lastname = str(input("last"))
        self.age = int(input("age"))


class Employee_details(Person):
    def get_employee_details(self):
        self.employee_id = int(input("employee_id"))
        self.salary = int(input("salary"))
        self.workphonenumber = int(input("workphonenumber"))


class Professor(Employee_details):
    def display(self):
        self.department = str(input("department"))
        self.branch = str(input("branch"))
        self.section = chr("section")
        print("firstname:", self.name)
        print("lastname:", self.lastname)
        print("age:", self.age)
        print("Employee_details",self.employee_id+" ,"+self.department+" ,"+self.branch+" ,"+self.section)
        print("workphonenumber",self.workphonenumber)
        print("salary",self.salary)
derived=Professor()
derived.get_details()
derived.get_employee_details()
derived.display()

