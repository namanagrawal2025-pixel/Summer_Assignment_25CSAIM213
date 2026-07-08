def add_student_record(rolls, names, courses):
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    course = input("Enter course name: ")
    rolls.append(roll)
    names.append(name)
    courses.append(course)
    print("Record added!")

def search_student_record(rolls, names, courses):
    search_roll = input("Enter roll number to search: ")
    if search_roll in rolls:
        idx = rolls.index(search_roll)
        print("Name:", names[idx], "| Course:", courses[idx])
    else:
        print("Record not found.")

def student_record_system():
    rolls = []
    names = []
    courses = []
    while True:
        print("\n1. Add Record\n2. Search Record\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student_record(rolls, names, courses)
        elif choice == "2":
            search_student_record(rolls, names, courses)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    student_record_system()

main()
