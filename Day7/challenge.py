class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def print_statement(self):
        print("Welcome to the ATM")
        print(f"Account statement for {self.firstname} {self.lastname}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

    def deposite(self, amount):
        if amount <= 0:
            print("Deposite must be in positive")
        else:
            self.balance += amount
            print(f"Credited: Rs {amount}/-. New balance: Rs {self.balance}/-")



    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficiant Balance")
        elif amount <= 0:
            print("Withdraw amount must be in positive")
        else:
            self.balance -= amount
            print(f"Desposited: Rs {amount}/-. New Balance: Rs {self.balance}")


def create_user():
    print("=== Create New Customer ===")
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    account_number = input("Enter account number: ")

    while True:
        try:
            balance = float(input("Enter initial balance: "))
            if balance < 0:
                print("Balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for balance.")

    print("Customer created successfully!\n")
    return Customer(firstname, lastname, account_number, balance)


# Function to start the ATM session
def start():
    customer = create_user()

    while True:
        print("\n=== ATM Menu ===")
        print("1. View Account Statement")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            customer.print_statement()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                customer.deposite(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                customer.withdraw(amount)
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# Start the program
start()