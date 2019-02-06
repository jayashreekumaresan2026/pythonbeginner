class Account:
    def __init__(self, account_type, account_no):
        self.account_no = account_no
        self.account_type = account_type

    def get_details(self):
        if self.account_no == "xxxxxxyyyyyy":
            print("valid user")
        else:
            print("enter valid account_no")


class Bank:
    def __init__(self, branch, holder_name,Account):
        self.branch = branch
        self.holder_name = holder_name
        self.account=Account

    def bank_details(self):
        print(self.account.get_details())


ob1 = Account("savings", "xxxxxxyyyyyy")
ob2 = Bank("canara", "yyyyyy",ob1)
ob2.bank_details()
