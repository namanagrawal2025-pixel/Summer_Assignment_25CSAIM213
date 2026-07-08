def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    employees[emp_id] = {"Name": name, "Dept": dept}
    print("Employee added successfully!")

def display_employees(employees):
    if not employees:
        print("No employee data available.")
        return
    for emp_id, info in employees.items():
        print("ID:", emp_id, "| Name:", info["Name"], "| Dept:", info["Dept"])

def employee_system():
    employees = {}
    while True:
        print("\n1. Add Employee\n2. Display Employees\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    employee_system()

main()
