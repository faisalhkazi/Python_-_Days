from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        return (f"Name: {self.firstname} {self.lastname}<br>"
                f"Account Number: {self.account_number}<br>"
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

# Global variable to store the customer
customer = None

# --- Routes ---

@app.route("/", methods=["GET", "POST"])
def index():
    global customer
    message = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create":
            firstname = request.form.get("firstname")
            lastname = request.form.get("lastname")
            account_number = request.form.get("account_number")
            try:
                balance = float(request.form.get("balance"))
                if balance < 0:
                    raise ValueError
            except:
                message = "Invalid balance amount."
                return render_template("index.html", message=message, customer=customer)

            customer = Customer(firstname, lastname, account_number, balance)
            message = "Customer created successfully."

        elif action == "deposit":
            if customer:
                try:
                    amount = float(request.form.get("deposit_amount"))
                    message = customer.deposit(amount)
                except:
                    message = "Invalid deposit amount."
            else:
                message = "Create an account first."

        elif action == "withdraw":
            if customer:
                try:
                    amount = float(request.form.get("withdraw_amount"))
                    message = customer.withdraw(amount)
                except:
                    message = "Invalid withdrawal amount."
            else:
                message = "Create an account first."

        elif action == "statement":
            if customer:
                message = customer.print_statement()
            else:
                message = "No customer account found."

    return render_template("index.html", message=message, customer=customer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
