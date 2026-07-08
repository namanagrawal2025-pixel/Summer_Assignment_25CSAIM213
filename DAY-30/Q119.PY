def insert_employee(ids, names):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    ids.append(emp_id)
    names.append(name)
    print("Employee added!")

def remove_employee(ids, names):
    emp_id = input("Enter employee ID to remove: ")
    if emp_id in ids:
        idx = ids.index(emp_id)
        ids.pop(idx)
        names.pop(idx)
        print("Employee removed successfully.")
    else:
        print("Employee ID not found.")

def mini_employee_system():
    ids = []
    names = []
    while True:
        print("\n1. Add Employee\n2. Remove Employee\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            insert_employee(ids, names)
        elif choice == "2":
            remove_employee(ids, names)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    mini_employee_system()

main()
