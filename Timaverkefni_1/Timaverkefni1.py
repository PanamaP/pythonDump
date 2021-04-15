# Elfar Snær Arnarson
# 10 febrúar 2020
# Tímaverkefni 1

class Account:
    def __init__(self):
        self.balance = 100.0

    def credit(self):  # Deposit
        print(self.balance)
        add = int(input("Enter amount to deposit: "))
        self.balance += add

    def debit(self):  # Withdraw
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw > self.balance:
            print("Debit amount exceeded account balance")
        else:
            self.balance -= withdraw
            print(f'Amount {withdraw} has been withdrawn')


class SavingAccount(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.04  # %
        self.amount = 0

    def calculateInterest(self):
        self.amount = self.balance * self.interest_rate
        return self.amount

        #   elf.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self):
        super().__init__()
        self.fee = 5

    def credit(self):  # account.credit
        add = int(input("Enter amount to deposit: "))
        self.balance += add
        fees = self.fee - SavingAccount().calculateInterest()
        self.balance = self.balance - fees
        print(f'{add}$ has been deposited')
        print(f'{fees}$ fee has been withdrawn from the deposit')

    def debit(self):  # withdrawn = Account.debit
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw > self.balance:
            print("Debit amount exceeded account balance")
        else:
            self.balance = self.balance - withdraw
            self.balance = self.balance - self.fee
            print(f'Amount {withdraw}$ has been withdrawn plus fee')
        return self.balance
        #  if (withdrawn   ):
        #  self.balance -= self.fee

    def prentaBalance(self):
        print(f'Current balance is: {self.balance}$')


'''checkingAcc = CheckingAccount()
savingAcc = SavingAccount()

print(savingAcc.calculateInterest())

checkingAcc.prentaBalance()

checkingAcc.debit()

checkingAcc.credit()
checkingAcc.prentaBalance()'''
