class ATM:
    def __init__(self, pin, balance=0):
        # Initialize the ATM with a PIN, balance, and transaction history
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
    def check_pin(self, entered_pin):
        # Check if the entered PIN matches the stored PIN
        return self.pin == entered_pin
    def balance_inquiry(self):
        # Display the current balance and add the transaction to history
        print(f"Your current balance is: ₹{self.balance}")
        self.transaction_history.append(f"Balance Inquiry: ₹{self.balance}")
    def cash_withdrawl(self, amount):
        # Withdraw the specified amount if balance is sufficient
        if amount > self.balance:
            print("Insufficient Balance...")
        else:
            self.balance -= amount
            print(f"₹{amount} has been withdrawn. Your new balance is ₹{self.balance}.")
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
    def cash_deposit(self, amount):
        # Deposit the specified amount into the balance and update transaction history
        self.balance += amount
        print(f"₹{amount} has been deposited. Your new balance is ₹{self.balance}.")
        self.transaction_history.append(f"Deposited: ₹{amount}")
    def change_pin(self, old_pin, new_pin):
        # Change the PIN if the old PIN is correctly entered
        if self.check_pin(old_pin):
            self.pin = new_pin
            print("Your PIN has been changed successfully.")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect old PIN.")
    def show_transaction_history(self):
        # Display all past transactions
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)
def main():
    # Initialize the ATM with a starting balance and predefined PIN
    user_pin = 1234
    atm = ATM(pin=user_pin, balance=5000)  # Starting balance of ₹5000
    print("Welcome to the ATM Machine Simulation.")
    # Infinite loop to continuously show the ATM menu until the user exits
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = int(input("Please choose an option: "))
        # Handle the user's menu selection
        if choice == 1:
            # Check balance
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                atm.balance_inquiry()
            else:
                print("Incorrect PIN.")
        elif choice == 2:
            # Withdraw cash
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                amount = int(input("Enter amount to withdraw: ₹"))
                atm.cash_withdrawl(amount)
            else:
                print("Incorrect PIN.")
        elif choice == 3:
            # Deposit cash
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                amount = int(input("Enter amount to deposit: ₹"))
                atm.cash_deposit(amount)
            else:
                print("Incorrect PIN.")
        elif choice == 4:
            # Change PIN
            entered_pin = int(input("Enter your current PIN: "))
            if atm.check_pin(entered_pin):
                new_pin = int(input("Enter new PIN: "))
                atm.change_pin(entered_pin, new_pin)
            else:
                print("Incorrect current PIN.")
        elif choice == 5:
            # Show transaction history
            entered_pin = int(input("Enter your PIN: "))
            if atm.check_pin(entered_pin):
                atm.show_transaction_history()
            else:
                print("Incorrect PIN.")
        elif choice == 6:
            # Exit the program
            print("Thank you for using the ATM. GoodBye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid Option. Please try again.")
# Entry point of the program
if __name__ == "__main__":
    main()
