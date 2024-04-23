# practise 01

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum/3
        print(f"avg marks of {self.name} is",avg)

s1 = student("ram",[95,90,85])
s1.get_avg()


# practise 02
class account:
    def __init__(self,acc_blc,bank_acc):
        self.balance = acc_blc
        self.bank_acc = bank_acc

    def credit(self,amount):
        self.balance += amount
        print(f"{amount} is credited to account {self.bank_acc}")
        print(f"Now, You have {self.balance} in your account")

    def debit(self,amount):
        self.balance -= amount
        print(f"{amount} is debited from account {self.bank_acc}")
        print(f"Now, you have {self.balance} in your account")

    def get_remain_money(self):
        return self.balance



s1 = account(10000,12899821)
s1.credit(1000)
s1.debit(1000)
