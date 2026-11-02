class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        print(self.name, "has balance:", self.balance)
    def deposit(self, depositamount):
        if depositamount <= 0:
            print("Amount must be greater than ZERO")           
        else:
            self.balance = self.balance + depositamount
            print("Amount Deposited Successfully!")
    def withdraw(self, wamount):
        if wamount <= 0:
            print("Amount must be greater than ZERO")
        elif wamount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance = self.balance - wamount
            print("Withdrawal Successful!")
            
acc = BankAccount("Thanesh", 50000)
acc.show_balance()
print("=================================")

depositamount = int(input("How much do you want to deposit? "))
acc.deposit(depositamount)
acc.show_balance()

print("=================================")
wamount = int(input("How much do you want to withdraw? "))
acc.withdraw(wamount)
acc.show_balance()
