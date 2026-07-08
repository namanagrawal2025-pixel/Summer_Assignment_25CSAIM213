def add_student(records):
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    records[roll] = {"Name": name, "Course": course}
    print("Student record added successfully!")

def view_students(records):
    if not records:
        print("No records found.")
        return
    for roll, details in records.items():
        print("Roll:", roll, "| Name:", details["Name"], "| Course:", details["Course"])

def student_system():
    records = {}
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student(records)
        elif choice == "2":
            view_students(records)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    student_system()

main()
