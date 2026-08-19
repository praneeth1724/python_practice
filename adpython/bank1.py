class BankAccount:
    def __init__(self, account_number,balance,amount):
        self.account_number = account_number
        self.balance = balance
        self.am = amount

    def bal(self):
        print(f"your account balance is {self.balance}")
     
    def deposit(self):
        self.balance = self.balance + self.am
        print(f"your account balance is {self.balance}")

    def withdraw(self):
        if self.balance < 0:
            raise ValueError("insufficent")
        try:
            self.balance = self.balance - self.am
        except ValueError as insuff:
            print(insuff)
        else:
            print(f"Your account balance {self.balance}")

print("Enter the task you want to perform \n 1.To check your balance \n 2.to deposit \n 3.withdraw")
task = int(input("enter:"))
if task == 1:
    acc = int(input("enter your account number:"))
    balance = 1000
    user1 = BankAccount(acc,balance,0)  
    user1.bal()
elif task == 2:
     acc = int(input("enter your account number:"))
     balance = 1000
     am = int(input("enter amount:"))
     user1 = BankAccount(acc,balance,am)
     user1.deposit()
elif task == 3:
     acc = int(input("enter your account number:"))
     balance = 1000
     witham = int(input("enter amount:"))
     user1 = BankAccount(acc,balance,witham)
     user1.withdraw()
else:
    print(f"invalid option {task}")
      
