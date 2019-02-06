class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def getdetails(self):
        print( self.firstname + " " + self.lastname + " " + self.age)


class PersonalDetails(Person):
    def __init__(self, email_id, phonenumber, address):
        self.email_id = email_id
        self.phonenumber = phonenumber
        self.address = address

    def get_personal_info(self):
        return self.getdetails() + " ," + self.phonenumber + self.address


class Employee_details(Person, PersonalDetails):
    def __init__(self, first, last, age, email_id, phonenumber, address):
        Person.__init__(self, first, last, age)
        PersonalDetails.__init__(self, email_id, phonenumber, address)


derived_class = Employee_details("jaya", 'shree', '21', 1999, "0000000", "some_address")
print(derived_class.getdetails())
print(derived_class.get_personal_info())
