def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    contacts[name] = phone
    print("Contact saved successfully!")

def search_contact(contacts):
    name = input("Enter Name to search: ")
    if name in contacts:
        print("Name:", name, "| Phone:", contacts[name])
    else:
        print("Contact not found.")

def contact_system():
    contacts = {}
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

def main():
    contact_system()

main()
