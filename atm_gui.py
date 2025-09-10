import tkinter as tk
from tkinter import messagebox

# --- Backend Classes ---

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
        return (f"Name: {self.firstname} {self.lastname}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: Rs {self.balance}/-")

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        return f"Deposited Rs {amount}/-. New balance: Rs {self.balance}/-"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Withdrawn Rs {amount}/-. New balance: Rs {self.balance}/-"

# --- UI Code ---

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.customer = None

        # Create Frames
        self.create_user_frame = tk.Frame(root)
        self.atm_frame = tk.Frame(root)

        self.build_create_user_frame()
        self.build_atm_frame()

        self.create_user_frame.pack()

    def build_create_user_frame(self):
        tk.Label(self.create_user_frame, text="Create New Customer", font=("Helvetica", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.create_user_frame, text="First Name:").grid(row=1, column=0, sticky="e")
        self.first_name_entry = tk.Entry(self.create_user_frame)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.create_user_frame, text="Last Name:").grid(row=2, column=0, sticky="e")
        self.last_name_entry = tk.Entry(self.create_user_frame)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.create_user_frame, text="Account Number:").grid(row=3, column=0, sticky="e")
        self.account_number_entry = tk.Entry(self.create_user_frame)
        self.account_number_entry.grid(row=3, column=1)

        tk.Label(self.create_user_frame, text="Initial Balance:").grid(row=4, column=0, sticky="e")
        self.balance_entry = tk.Entry(self.create_user_frame)
        self.balance_entry.grid(row=4, column=1)

        tk.Button(self.create_user_frame, text="Create Account", command=self.create_account).grid(row=5, columnspan=2, pady=10)

    def build_atm_frame(self):
        tk.Label(self.atm_frame, text="ATM Operations", font=("Helvetica", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Button(self.atm_frame, text="View Statement", command=self.view_statement).grid(row=1, columnspan=2, pady=5)

        tk.Label(self.atm_frame, text="Deposit Amount:").grid(row=2, column=0)
        self.deposit_entry = tk.Entry(self.atm_frame)
        self.deposit_entry.grid(row=2, column=1)
        tk.Button(self.atm_frame, text="Deposit", command=self.make_deposit).grid(row=3, columnspan=2, pady=5)

        tk.Label(self.atm_frame, text="Withdraw Amount:").grid(row=4, column=0)
        self.withdraw_entry = tk.Entry(self.atm_frame)
        self.withdraw_entry.grid(row=4, column=1)
        tk.Button(self.atm_frame, text="Withdraw", command=self.make_withdrawal).grid(row=5, columnspan=2, pady=5)

        tk.Button(self.atm_frame, text="Exit", command=self.root.quit).grid(row=6, columnspan=2, pady=10)

    def create_account(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        account_number = self.account_number_entry.get()
        try:
            balance = float(self.balance_entry.get())
            if balance < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for balance.")
            return

        if not firstname or not lastname or not account_number:
            messagebox.showerror("Error", "All fields must be filled.")
            return

        self.customer = Customer(firstname, lastname, account_number, balance)
        messagebox.showinfo("Success", "Customer account created!")
        self.create_user_frame.pack_forget()
        self.atm_frame.pack()

    def view_statement(self):
        if self.customer:
            messagebox.showinfo("Account Statement", self.customer.print_statement())

    def make_deposit(self):
        try:
            amount = float(self.deposit_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")
            return

        result = self.customer.deposit(amount)
        messagebox.showinfo("Deposit", result)

    def make_withdrawal(self):
        try:
            amount = float(self.withdraw_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")
            return

        result = self.customer.withdraw(amount)
        messagebox.showinfo("Withdraw", result)


# --- Run the App ---

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
