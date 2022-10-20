class Account:
    latestAccNum = 1000000
    overdraftLim = -1000
    def __init__(self, fName, lName):
        if fName == "" or lName == '':
            raise Exception("Invalid altribute")
        self.accNum = Account.latestAccNum
        self.fName = fName
        self.lName = lName
        self.balance = 0
        Account.latestAccNum += 1

    def getAccNum(self):
        return self.accNum
    
    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def getBalance(self):
        return self.balance

    def setFName(self, fName):
        if fName == "":
            raise Exception("Cannot set empty first name!")
        self.fName = fName
        print("Successfully set first name!")

    def setLName(self, lName):
        if lName == "":
            raise Exception("Cannot set empty last name!")
        self.lName = lName
        print("Successfully set last name!")

    def displayAccount(self):
        print(f"{self.accNum}", f"\t{self.fName}", f"\t{self.lName}", f"\t{self.balance}")

    def deposit(self, dAmt):
        if dAmt < 0:
            raise Exception("Cannot deposit negative amount!")
        self.balance += dAmt
        print(f"Successfully deposit ${dAmt}!")

    def withdraw(self):
        print("Warning! This is an abstract method.")

class ChequingAccount(Account):
    def __init__(self, fName, lName):
        super().__init__(fName, lName)

    def withdraw(self, wdAmt):
        if wdAmt < 0:
            raise Exception("Cannot withdraw negative amount!")
        if self.balance-wdAmt < Account.overdraftLim:
            raise Exception("Balance below overdraft limit!")
        self.balance -= wdAmt
        print(f"Successfully withdraw ${wdAmt}!")

class SavingAccount(Account):
    def __init__(self, fName, lName):
        super().__init__(fName, lName)
        self.withdrawFee = 0

    def setWidthdrawFee(self, wdFee):
        self.withdrawFee = wdFee

    def withdraw(self, wdAmt):
        if wdAmt < 0:
            raise Exception("Cannot withdraw negative amount!")
        if wdAmt > 0:
            if self.balance < Account.overdraftLim:
                self.balance -= wdAmt + 5*self.withdrawFee
            else:
                self.balance -= wdAmt + self.withdrawFee

def test():
    myChequeAccount = ChequingAccount("Leonard", "Ji")
    myChequeAccount.setLName("Chi")
    myChequeAccount.deposit(1000000)
    #myChequeAccount.withdraw(1000000+1000+1)
    myChequeAccount.displayAccount()

    mySavingAccount = SavingAccount("Leonard", "Chi")
    mySavingAccount.setWidthdrawFee(5)
    mySavingAccount.withdraw(1000)
    print(mySavingAccount.getBalance())
    mySavingAccount.withdraw(5)
    mySavingAccount.displayAccount()


def main():
    test()

if __name__ == "__main__":
    main()