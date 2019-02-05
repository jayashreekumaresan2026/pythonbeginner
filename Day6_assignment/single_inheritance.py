class person():
    def __int__(self, name, email_address, phone_number,address):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
        self.address = address

    def get_details(self):
        print("The name of the employee:", self.name)
        print("Email_address:", self.email_address)
        print("Phone_number:", self.phone_number)
        print("Address of the person", self.address)


class is_employee(person):
    def __init__(self, name, email_address, phone_number, address, employee_id, salary):
        person.__int__(self, name, email_address, phone_number, address)
        self.employee_id = employee_id
        self.salary = salary

    def get_employee(self):
        return self.get_details() + "," + self.employee_id + "," + self.salary


first_class = person('jaya',"jayashree.2026","000000000000","someaddress")
second_class =is_employee("1086", "somesalary")
print(first_class.get_details())
print(second_class.get_employee())
