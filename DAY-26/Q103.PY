def atm_simulation():
    balance = 5000
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("Current Balance:", balance)
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Deposited successfully. New Balance:", balance)
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawn successfully. Remaining Balance:", balance)
            else:
                print("Insufficient balance!")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice!")

def main():
    atm_simulation()

main()
