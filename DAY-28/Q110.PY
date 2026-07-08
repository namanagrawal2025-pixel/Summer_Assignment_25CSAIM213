def create_account(accounts):
    acc_num = input("Enter Account Number: ")
    name = input("Enter Holder Name: ")
    accounts[acc_num] = {"Name": name, "Balance": 0.0}
    print("Account created successfully!")

def deposit_money(accounts):
    acc_num = input("Enter Account Number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["Balance"] += amount
        print("Amount deposited. Current Balance:", accounts[acc_num]["Balance"])
    else:
        print("Account not found.")

def bank_system():
    accounts = {}
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    bank_system()

main()
