'''Create a class "BankAccount" with attributes account number and balance. Implement
methods to deposit and withdraw funds, and a display method to show the account details.
'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds for the withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")

def main():
    account_number = input("Enter your account number: ")
    balance = float(input("Enter the initial balance (default 0): ") or 0)
    account = BankAccount(account_number, balance)

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit funds")
        print("2. Withdraw funds")
        print("3. Display account details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
