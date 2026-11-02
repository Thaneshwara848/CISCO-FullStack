
class BankAccount :
    def __init__(self,name, balance ):
        print("Hi This is Constructor....! we are initiliing globly at once ")
        self.name = name ; 
        self.balance = balance;
    def showbalance(self) :
        print("HI This is balance Method Method ")
        print(self.name, "has balance " , self.balance);
        
        
acc1 = BankAccount("Thanesh",500000); # as soon as we create obj then constructor will call 
acc1.showbalance(); # using the  refrence of object  we call the method
#acc1.showbalance(); #using this refrence we can call multiple with single obj refrence 
#acc1.showbalance();

print("========================")

acc2 = BankAccount("Ramesh",600000);
acc2.showbalance();