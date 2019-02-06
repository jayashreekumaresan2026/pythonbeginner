class Account:
    def __init__(self, account_type, account_no):
        self.account_no = account_no
        self.account_type = account_type

    def get_details(self):
        if self.account_no == "012345":
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
        print(self.holder_name)
        print(self.branch)
        print(self.Account.account_no)



ob1 = Account("savings", "012345")
ob2 = Bank("canara_bank", "jaya",ob1)
ob2.bank_details()
