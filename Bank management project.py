import datetime

# ---------- Transaction Class ----------
class Transaction:
    def __init__(self, t_type, amount, balance):
        self.type = t_type
        self.amount = amount
        self.date = datetime.datetime.now()
        self.balance = balance

    def show(self):
        print(self.date, "|", self.type, "|", self.amount, "| Balance:", self.balance)


# ---------- BankAccount Class ----------
class BankAccount:
    def __init__(self, name, acc_no, deposit, acc_type):
        self.name = name                  # public
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.__balance = deposit          # private
        self.transactions = []

        self.transactions.append(Transaction("Account Created", deposit, self.__balance))

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.__balance += amount
        self.transactions.append(Transaction("Deposit", amount, self.__balance))
        print("Deposit successful")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount
        self.transactions.append(Transaction("Withdraw", amount, self.__balance))
        print("Withdraw successful")

    def transfer(self, target, amount):
        if amount > self.__balance:
            print("Not enough balance")
            return
        self.__balance -= amount
        target.__balance += amount

        self.transactions.append(Transaction("Transfer Sent", amount, self.__balance))
        target.transactions.append(Transaction("Transfer Received", amount, target.__balance))
        print("Transfer successful")

    def interest(self):
        if self.acc_type == "Savings":
            interest = self.__balance * (0.04 / 12)
            self.__balance += interest
            self.transactions.append(Transaction("Interest Added", interest, self.__balance))

    def mini_statement(self):
        print("\nMini Statement:")
        for t in self.transactions[-5:]:
            t.show()

    def full_statement(self):
        print("\nFull Statement:")
        for t in self.transactions:
            t.show()


# ---------- Bank Class ----------
class Bank:
    def __init__(self):
        self.name = "Sonia Bank"
        self.accounts = {}
        self.next_acc_no = 1001

    def create_account(self, name, deposit, acc_type):
        if deposit < 1000:
            print("Minimum deposit is 1000")
            return None
        acc = BankAccount(name, self.next_acc_no, deposit, acc_type)
        self.accounts[self.next_acc_no] = acc
        self.next_acc_no += 1
        return acc.acc_no

    def find(self, acc_no):
        return self.accounts.get(acc_no)


# ---------- MAIN PROGRAM ----------
bank = Bank()

while True:
    print("\nWelcome to", bank.name)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Mini Statement")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        dep = int(input("Initial deposit: "))
        acc_type = input("Savings / Checking: ")
        acc_no = bank.create_account(name, dep, acc_type)
        if acc_no:
            print("Account Created")
            print("Account Number:", acc_no)

    elif choice == "2":
        acc = int(input("Account number: "))
        amt = int(input("Amount: "))
        bank.find(acc).deposit(amt)

    elif choice == "3":
        acc = int(input("Account number: "))
        amt = int(input("Amount: "))
        bank.find(acc).withdraw(amt)

    elif choice == "4":
        src = int(input("Your account number: "))
        tgt = int(input("Target account number: "))
        amt = int(input("Amount: "))
        bank.find(src).transfer(bank.find(tgt), amt)

    elif choice == "5":
        acc = int(input("Account number: "))
        print("Balance:", bank.find(acc).get_balance())

    elif choice == "6":
        acc = int(input("Account number: "))
        bank.find(acc).mini_statement()

    elif choice == "7":
        print("Thank you for using Sonia Bank.........")
        break

    else:
        print("Invalid choice")
