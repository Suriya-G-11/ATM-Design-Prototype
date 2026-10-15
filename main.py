from calc import deposit, withdraw, check_balance

def atm():

    balance = 3000.00
    correct_pin = "1234"
    print("Welcome to GBS Bank!")

    card = input("Please insert your card (yes/no): ").strip().lower()

    if card not in ["yes", "y"]:
        print("Transaction cancelled.")
        print("Thank you for choosing our ATM! Have a nice day.")
        return

    print("Reading your card...")

    pin = input("Enter your 4-digit PIN: ").strip()

    if pin != correct_pin:
        print("Incorrect PIN!")
        print("Transaction cancelled.")
        print("Thank you for choosing our ATM! Have a nice day.")
        return

    print("PIN verified successfully!")

    while True:

        print("\n========== MAIN MENU ==========")
        print("D  - Cash Deposit")
        print("W  - Cash Withdraw")
        print("CB - Check Balance")
        print("================================")

        choice = input("Choose your transaction: ").strip().lower()

            
        if choice in ["d", "deposit", "cash deposit"]:
            print(f"Available balance before deposit: ₹{balance:.2f}")
            amount = float(input("Enter deposit amount: ₹"))

            if amount > 0:
                balance = deposit(balance, amount)
                print(f"Deposit successful: ₹{amount:.2f}")
                print(f"Available balance after deposit: ₹{balance:.2f}")
            else:
                print("Please enter a valid amount!")

        elif choice in ["w", "withdraw", "cash withdraw"]:
            print(f"Available balance before withdrawal: ₹{balance:.2f}")
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= 0:
                print("Please enter a valid amount!")

            elif amount > balance:
                print("Insufficient balance!")
                print(f"Available balance: ₹{balance:.2f}")
            else:
                balance = withdraw(balance, amount)
                print(f"Withdrawal successful: ₹{amount:.2f}")
                print(f"Available balance after withdrawal: ₹{balance:.2f}")

        elif choice in ["cb", "balance", "cash balance", "check balance"]:
            print(f"Your current account balance is: ₹{check_balance(balance):.2f}")
        
        else:
            print("Invalid option! Please choose D, W, or CB.")
            continue
           
        again = input(
            "\nDo you want to continue? (yes/no): "
            ).strip().lower()

        if again not in ["yes", "y"]:
            break
            
    print("\nThank you for choosing our ATM! Have a nice day.")

if __name__ == "__main__":
    atm()