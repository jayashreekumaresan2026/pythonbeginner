class Person:
    def get_details(self):
        self.firstname = str(input("first"))
        self.lastname = str(input("last"))
        self.age = int(input("age"))

    def show_person_detail(self):
        print("firstname:", self.name)
        print("lastname:", self.lastname)
        print("age:", self.age)


class Employee_details(Person):
    def get_employee_details(self):
        self.employee_id = int(input("employee_id"))
        self.salary = int(input("salary"))
        self.workphonenumber = int(input("workphonenumber"))

    def show_employee_detail(self):
        print("employee_id", self.employee_id)
        print("workphonenumber", self.workphonenumber)
        print("salary", self.salary)


class Professor(Person):
    def professor_details(self):
        self.department = str(input("department"))
        self.branch = str(input("branch"))
        self.section = chr("section")

    def show_professor_details(self):
        print(self.department + " ," + self.branch + " ," + self.section + ",")


class secretory(Person):
    def secretory_details(self):
        self.college = str(input("college"))

    def display(self):
        print("Employee_college", self.college)


base = Person()
derived1 = Employee_details()
derived2 = Professor()
derived3 = secretory()
base.get_details()
base.show_person_detail()
derived1.get_employee_details()
derived1.show_employee_detail()
derived2.professor_details()
derived2.show_professor_details()
derived3.secretory_details()
derived3.display()
