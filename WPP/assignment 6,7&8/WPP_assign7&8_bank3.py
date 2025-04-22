'''Write a Python program to create a class representing a bank. Include methods for managing
customer accounts and transactions.
'''

class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited, Current balance: {self.balance}")
        else:
            print("Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn, Current balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Transfer amount should be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance to transfer.")
        else:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transferred {amount} to account {other_account.account_number}.")
            print(f"Your new balance: {self.balance}")


class Bank:
    def __init__(self):
        self.customers = {}  

    def create_account(self, name, account_number):

        if account_number in self.customers:
            print("Account with this account number already exists.")
        else:
            self.customers[account_number] = Customer(name, account_number)
            print(f"Account created for {name} with account number: {account_number}")

    def get_customer(self, account_number):
        
        return self.customers.get(account_number, None)

    def display_all_accounts(self):
        
        if not self.customers:
            print("No accounts found.")
        else:
            for account_number, customer in self.customers.items():
                print(f"Account Number: {account_number}, Name: {customer.name}, Balance: {customer.get_balance()}")

def main():
    bank = Bank()

    while True:
        print("\nBanking System Operations:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Display All Accounts")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the customer's name: ")
            account_number = input("Enter the account number: ")
            bank.create_account(name, account_number)
            
        elif choice == '2':
            account_number = input("Enter the account number: ")
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter the amount to deposit: "))
                customer.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter the account number: ")
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter the amount to withdraw: "))
                customer.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number_from = input("Enter the account number to transfer from: ")
            account_number_to = input("Enter the account number to transfer to: ")
            customer_from = bank.get_customer(account_number_from)
            customer_to = bank.get_customer(account_number_to)
            if customer_from and customer_to:
                amount = float(input("Enter the amount to transfer: "))
                customer_from.transfer(amount, customer_to)
            else:
                print("One or both accounts not found.")

        elif choice == '5':
            account_number = input("Enter the account number: ")
            customer = bank.get_customer(account_number)
            if customer:
                print(f"Balance for account {account_number}: {customer.get_balance()}")
            else:
                print("Account not found.")

        elif choice == '6':
            bank.display_all_accounts()

        elif choice == '7':
            print("Exiting... Thank you for using the banking system!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
