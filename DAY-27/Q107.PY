def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.50
    gross = basic + hra + da
    return gross

def salary_system():
    salaries = {}
    while True:
        print("\n1. Calculate & Store Salary\n2. View Salary Records\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter Employee Name: ")
            basic = float(input("Enter Basic Salary: "))
            gross = calculate_salary(basic)
            salaries[name] = gross
            print("Salary processed!")
        elif choice == "2":
            for name, gross in salaries.items():
                print("Employee:", name, "| Gross Salary:", gross)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    salary_system()

main()
