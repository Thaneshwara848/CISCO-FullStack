class Bank :
    def deposit(self,amount):
        print("Despoited  : " ,amount );
        self.amount=amount;
        
    def Checkbalance(self):
        print("Check balance ", self.amount )
        
    def withdraw(self,wAmount):
        print("withdrawl amoaunt :" ,wAmount);
        self.amount= self.amount-wAmount;


b1 = Bank();
depAmount= int(input("How much You Want to Deposit : "))
b1.deposit(depAmount);  #-10000 
print("========After Deposit You balalce is ======= ")     
b1.Checkbalance();
withdrawAmount=int(input("How much AMount You Want WithDraw"));
b1.withdraw(withdrawAmount) 
print("========After WithDraw You balalce is ======= ")     
b1.Checkbalance();



