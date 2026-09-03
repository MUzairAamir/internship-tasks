#Build a BankAccount class with a private balance, 
#and deposit()/withdraw() methods that never allow the balance
# to go negative.
class BankAccount:
    def __init__(self, balance, acc_num, name, city, cnic):
        self.name = name
        self.city = city
        self.cnic = cnic
        self.acc_num = acc_num
        self.__balance = balance
# creating a constructor to initialize the balance, account number, name, city and cnic of the customer
#balance is private variable and can only be accessed within the class
#blance should not be negative, if it is negative then it should be set to zero and a message should be printed
        if balance < 0:
            print("kam se kam zero tu rakho payare ")
            print(f"invalid balance for Customer name {self.name} account number: {self.acc_num}")
            self.__balance = 0

  # creating deposit funtion to deposit money in the account          

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Your updated balance is ",self.__balance)
            print("Deposit Successfully")
        elif amount < 0:
            print("khair ha negative ma hi kari ja rahe ho")
# creating withdraw funtion to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("withdraw Successfully")
            print("Your updated balance is ",self.__balance)
        else:
            print("Insufficient balance or invalid amount")
# creating transfer funtion to transfer money from one account to another
    def transfer(self, receiver, amount):

        # Validation
        if amount <= 0:
            print("Invalid transfer amount")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        # Save old balances
        old_sender_balance = self.__balance
        old_receiver_balance = receiver.__balance

        try:
            # Transaction
            self.__balance -= amount
            receiver.__balance += amount

            print("Transfer Successfully")
            print("Your updated balance is ", self.__balance)

        except:
            # Rollback
            self.__balance = old_sender_balance
            receiver.__balance = old_receiver_balance
            print("Transaction failed. Money has been restored.")
# output of the program

print("hi User ")

c1=BankAccount(100,20001,"Uzair","Lahore",3520228670000)
c2=BankAccount(-1,83802239,"xccx","sc",234212)
#print(c1.__balance)
print("Hi wellcome to my banking company ")
print("Your account number is ",c1.acc_num)
c1.deposit(1000)

c1.withdraw(500)
c1.transfer(c2,400)

