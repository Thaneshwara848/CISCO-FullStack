
class Bank:

    def __init__(self):
        self.amount = 0

    def deposit(self, amount):
        if amount > 0:
            self.amount = self.amount + amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")
    def Checkbalance(self):
        print("Available Balance:", self.amount)

    def withdraw(self, wAmount):
        if wAmount <= 0:
            print("Invalid withdrawal amount")
        elif wAmount <= self.amount:
            self.amount = self.amount - wAmount
            print("Withdrawn Amount:", wAmount)
        else:
            print("Insufficient Balance")


# Create Object
b1 = Bank()

# Deposit
depAmount = int(input("How much do you want to deposit? "))
b1.deposit(depAmount)

print("====== After Deposit ======")
b1.Checkbalance()

# Withdrawal
withdrawAmount = int(input("How much do you want to withdraw? "))
b1.withdraw(withdrawAmount)

print("====== After Withdrawal ======")
b1.Checkbalance()





