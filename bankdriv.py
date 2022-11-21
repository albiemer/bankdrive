
import getpass


myinvalid = 0

while True:
    

    setname = input("Enter your Name: ")
    setpassword = getpass.getpass("Enter your Password: ")
    #setamount = input("Enter Amount: ")


    class account:
        myinvalidp = 0
        mypassword = "albi3mer"
        mybalance = 50

        def __init__(self, setpword, myinvalid):
            account.myinvalidp = myinvalid
            self.mypword = setpword
            #self.myamount = amount
                
        def getBalance(self, pword):
            if pword == self.mypword:
                account.mybalance -= account.myinvalidp
                return account.mybalance
            else:
                account.myinvalidp += 1
                account.mybalance -= account.myinvalidp
                return account.mybalance
    
    
    print(setname, "'s, balance is :", account(setpassword, myinvalid).getBalance( \
        account.mypassword))

    myinvalid = account.myinvalidp

    print("Result of invalid Password: ", account.myinvalidp)



