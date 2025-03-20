class BankAccount:
    def __init__(self, account_number: str, balance: float, date_of_opening: str, customer_name: str):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self.balance += amount
        return amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        if self.balance < amount:
            return "insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def customer_details(self):
        print("Customer Details:")
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")


# Example usage:
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount(account_number="43145623", balance=500.0,
                          date_of_opening="2025-3-20", customer_name="Peter Wambua")

    deposited_amount = account.deposit(4500.0)
    print(f"Deposited: {deposited_amount}")

    withdrawal = account.withdraw(3000.0)
    if withdrawal == "insufficient balance":
        print("Withdrawal failed: insufficient balance")
    else:
        print(f"Withdrawn: {withdrawal}")

    account.check_balance()

    account.customer_details()
