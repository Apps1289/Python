# PUBLIC AND PRIVATE IN OPPS

class account:
    def __init__(self,acc_no,acc_pwd):
        self.account_num = acc_no
        self.account_pwd = acc_pwd
s1 = account(12345,1289)
print(s1.account_num)
print(s1.account_pwd)

# here in above example we are able to access the account class' property outside the class, so here it is public

#> now lets make acc_pwd as private

class accounts:
    def __init__(self,acc_no,acc_pwd):
        self.account_num = acc_no
        self.__account_pwd = acc_pwd  #> giving two underscore before name makes it private
s1 = accounts(12345,1289)
print(s1.account_num)
print(s1.__account_pwd)


#> so for accessing such private values we can access it through methods inside the class and calling that function outside the class

class imp:
    def __init__(self,acc_no,acc_pwd):
        self.accounts_num = acc_no
        self.__accounts_pwd = acc_pwd

    def reset_pwd(self):
        print(self.__accounts_pwd)

s12 = imp("12345","1289")
print(s12.accounts_num)
print(s12.reset_pwd())