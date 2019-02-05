class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def getdetails(self):
        return self.firstname + " " + self.lastname + " " + self.age


class Personal_details(Person):
    def __init__(self, email_id, phonenumber, address):
        self.email_id = email_id
        self.phonenumber = phonenumber
        self.address = address

    def get_personal_info(self):
        return self.getdetails() + " ," + self.phonenumber + self.address


class Employee_details(Person, Personal_details):
    def __init__(self, first, last, age, email_id, phonenumber, address):
        Person.__init__(self, first, last, age)
        Personal_details.__init__(self, email_id, phonenumber, address)


derived_class = Employee_details("jaya", 'shree', '21', 1999, "0000000", "someaddress")
derived_class.getdetails()
derived_class.get_personal_info()
