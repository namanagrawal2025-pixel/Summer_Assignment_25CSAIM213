def insert_element(arr):
    elem = int(input("Enter element to insert: "))
    arr.append(elem)
    print("Element added.")

def delete_element(arr):
    elem = int(input("Enter element to delete: "))
    if elem in arr:
        arr.remove(elem)
        print("Element deleted.")
    else:
        print("Element not found.")

def display_array(arr):
    print("Current Array:", arr)

def array_system():
    arr = []
    while True:
        print("\n1. Insert\n2. Delete\n3. Display\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            insert_element(arr)
        elif choice == "2":
            delete_element(arr)
        elif choice == "3":
            display_array(arr)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def main():
    array_system()

main()
