# ATM Machine Simulation in Python

This project is an **ATM Machine Simulation** developed using Python, designed to perform basic ATM functions like balance inquiry, cash withdrawal, deposit, PIN change, and viewing transaction history.

## Features

1. **Balance Inquiry**: Check your current balance.
2. **Cash Withdrawal**: Withdraw a specified amount if sufficient balance is available.
3. **Cash Deposit**: Deposit a specified amount into the account.
4. **PIN Change**: Change the account PIN by verifying the current PIN.
5. **Transaction History**: View a record of past transactions.

## Project Structure

- **ATM Class**: Contains methods for all the features mentioned above.
  - `balance_inquiry()`: Displays current balance.
  - `cash_withdrawl(amount)`: Withdraws the specified amount.
  - `cash_deposit(amount)`: Deposits the specified amount.
  - `change_pin(old_pin, new_pin)`: Changes the user's PIN.
  - `show_transaction_history()`: Shows the transaction history.
- **Main Loop**: Provides an interactive menu for the user to choose actions like balance inquiry, deposit, etc.


